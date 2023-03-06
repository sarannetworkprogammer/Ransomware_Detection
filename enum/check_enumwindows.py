# code for API Enumwindows

import ctypes
import win32process
import psutil

# Constants for EnumWindows function
ENUM_WINDOWS_PROC = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GW_OWNER = 4

def find_processes_with_enum_windows():
    # Iterate over all running processes
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Open the process with PROCESS_QUERY_INFORMATION and PROCESS_VM_READ access
            hProcess = win32process.OpenProcess(win32process.PROCESS_QUERY_INFORMATION | win32process.PROCESS_VM_READ, False, proc.pid)

            # Get the module handle for user32.dll
            user32_handle = ctypes.windll.kernel32.GetModuleHandleA(b"user32.dll")

            # Get the address of EnumWindows
            EnumWindows_addr = ctypes.windll.kernel32.GetProcAddress(user32_handle, b"EnumWindows")

            # If EnumWindows is found in the process memory, check if the process has called it
            if EnumWindows_addr:
                buf = ctypes.create_string_buffer(4)

                def callback(hwnd, lParam):
                    pid = ctypes.c_ulong()
                    ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
                    if pid.value == proc.pid:
                        ctypes.windll.user32.GetWindow(hwnd, GW_OWNER)
                    return True

                enum_windows_proc = ENUM_WINDOWS_PROC(callback)
                ctypes.windll.kernel32.ReadProcessMemory(hProcess, EnumWindows_addr, buf, 4, None)
                func_ptr = ctypes.cast(buf, ctypes.POINTER(ctypes.c_void_p)).contents
                enum_windows_func = ENUM_WINDOWS_PROC(func_ptr)
                enum_windows_func(enum_windows_proc, 0)

                if callback.called:
                    print("Process {0} ({1}) has made an API call to EnumWindows".format(proc.name(), proc.pid))

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass