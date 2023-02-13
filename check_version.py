#checking getversion api is called or not
# checking which process get_version api

import ctypes
import psutil

# Define the API function we want to detect
kernel32 = ctypes.WinDLL("kernel32.dll")
GetVersion = kernel32.GetVersion
GetVersion.argtypes = []
GetVersion.restype = ctypes.c_ulong

# Iterate through the running processes
for proc in psutil.process_iter():
    try:
        version = GetVersion()
        if version:
            print("Process '{}' has called the GetVersion API".format(proc.name()))
            
    except:
        pass
