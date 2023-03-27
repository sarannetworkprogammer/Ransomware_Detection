

"""
This approach may not detect all processes that have called the GetUserNameA function,

 as some processes may be protected or obscured by security measures and may not be easily identifiable.
"""


import ctypes
import psutil

# Load the kernel32.dll library
kernel32 = ctypes.WinDLL('kernel32')

# Call the GetCurrentProcessId function to obtain the current process ID
pid = kernel32.GetCurrentProcessId()

# Iterate over all running processes and check for the GetUserNameA function
for proc in psutil.process_iter(['name']):
    try:
        # Check if the process has called the GetUserNameA function
        if 'advapi32.dll' in proc.memory_maps() and 'GetUserNameA' in proc.memory_maps()['advapi32.dll']:
            print(f"Process {proc.name()} ({proc.pid}) called GetUserNameA.")
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        pass
