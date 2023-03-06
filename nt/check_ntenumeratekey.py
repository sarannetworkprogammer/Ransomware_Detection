#python code for ntenumeratekey


import ctypes
import win32process
import psutil

def find_processes_with_NtEnumerateKey():
    # Iterate over all running processes
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Open the process with PROCESS_QUERY_INFORMATION and PROCESS_VM_READ access
            hProcess = win32process.OpenProcess(win32process.PROCESS_QUERY_INFORMATION | win32process.PROCESS_VM_READ, False, proc.pid)

            # Get the handle for ntdll.dll
            ntdll_handle = ctypes.windll.kernel32.GetModuleHandleA(b"ntdll.dll")

            # Get the address of NtEnumerateKey
            NtEnumerateKey_addr = ctypes.windll.kernel32.GetProcAddress(ntdll_handle, b"NtEnumerateKey")

            # If NtEnumerateKey is found in the process memory, check if the process has called it
            if NtEnumerateKey_addr:
                buf = ctypes.create_string_buffer(4)

                # Define the signature of the NtEnumerateKey function
                NtEnumerateKey_type = ctypes.WINFUNCTYPE(
                    ctypes.c_long,
                    ctypes.c_void_p,
                    ctypes.c_ulong,
                    ctypes.c_ulong,
                    ctypes.c_ulong,
                    ctypes.c_void_p,
                    ctypes.c_ulong,
                    ctypes.POINTER(ctypes.c_ulong),
                    ctypes.POINTER(ctypes.c_ulong))

                # Define a callback function that will be used to record the process id of the process that makes the API call
                def NtEnumerateKey_callback(KeyHandle, Index, KeyValueInformationClass, KeyValueName, Length, ResultLength):
                    if proc.pid == ctypes.windll.kernel32.GetCurrentProcessId():
                        return True
                    return False

                # Create a function pointer for the NtEnumerateKey function and cast it to the correct type
                func_ptr = ctypes.cast(NtEnumerateKey_addr, ctypes.POINTER(ctypes.c_void_p)).contents
                NtEnumerateKey_func = NtEnumerateKey_type(func_ptr)

                # Call the NtEnumerateKey function with the custom callback
                NtEnumerateKey_func(0, 0, 0, 0, 0, 0, 0, ctypes.pointer(NtEnumerateKey_callback))

                if NtEnumerateKey_callback.called:
                    print("Process {0} ({1}) has made an API call to NtEnumerateKey".format(proc.name(), proc.pid))

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass