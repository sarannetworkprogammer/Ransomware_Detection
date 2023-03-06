import ctypes
import win32process
import psutil

# Constants for CreateToolhelp32Snapshot function
TH32CS_SNAPPROCESS = 0x00000002

def find_processes_with_create_snapshot():
    # Iterate over all running processes
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Open the process with PROCESS_QUERY_INFORMATION and PROCESS_VM_READ access
            hProcess = win32process.OpenProcess(win32process.PROCESS_QUERY_INFORMATION | win32process.PROCESS_VM_READ, False, proc.pid)

            # Get the module handle for kernel32.dll
            kernel32_handle = ctypes.windll.kernel32.GetModuleHandleA(b"kernel32.dll")

            # Get the address of CreateToolhelp32Snapshot
            CreateToolhelp32Snapshot_addr = ctypes.windll.kernel32.GetProcAddress(kernel32_handle, b"CreateToolhelp32Snapshot")

            # If CreateToolhelp32Snapshot is found in the process memory, check if the process has called it
            if CreateToolhelp32Snapshot_addr:
                process_has_called_create_snapshot = False
                for thread in proc.threads():
                    try:
                        context = win32process.GetThreadContext(win32process.OpenThread(win32process.THREAD_ALL_ACCESS, False, thread.id))
                        instr_ptr = context.Eip
                        if instr_ptr >= CreateToolhelp32Snapshot_addr and instr_ptr < CreateToolhelp32Snapshot_addr + 20:
                            process_has_called_create_snapshot = True
                            break
                    except:
                        continue

                if process_has_called_create_snapshot:
                    print("Process {0} ({1}) has made an API call to CreateToolhelp32Snapshot".format(proc.name(), proc.pid))

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass