import psutil
import win32api
import win32con

# Get the address of the GetComputerNameW function
kernel32 = win32api.LoadLibrary("kernel32")

print(f"kernel32={kernel32}")

get_computername_addr = win32api.GetProcAddress(kernel32, "GetComputerNameW")

print(f"get_computername_addr={get_computername_addr}")




""" 

# Iterate over all running processes
for proc in psutil.process_iter(['pid', 'name', 'exe']):
    try:
        # Get the list of loaded modules for the process
        proc_modules = proc.memory_maps(grouped=False)

        # Check if the process has loaded kernel32.dll
        kernel32_loaded = any('kernel32.dll' in module.path for module in proc_modules)

        if kernel32_loaded:
            # Get the address of the GetComputerNameW function for the process
            proc_kernel32 = win32api.OpenProcess(win32con.PROCESS_VM_READ, False, proc.pid)
            proc_get_computername_addr = win32api.GetProcAddress(proc_kernel32, "GetComputerNameW")
            win32api.CloseHandle(proc_kernel32)

            # If the process has called GetComputerNameW, print its details
            if proc_get_computername_addr == get_computername_addr:
                print(f"Process {proc.name()} (PID {proc.pid}) has called GetComputerNameW.")
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        pass

   


"""