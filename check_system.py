import ctypes
import psutil

# Define the API function we want to detect
kernel32 = ctypes.WinDLL("kernel32.dll")
GetSystemInfo = kernel32.GetSystemInfo
GetSystemInfo.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
GetSystemInfo.restype = None

# Iterate through the running processes
for proc in psutil.process_iter():
    try:
        sys_info = ctypes.c_void_p()
        GetSystemInfo(ctypes.byref(sys_info))
        if sys_info.value:
            print("Process '{}' has called the GetSystemInfo API".format(proc.name()))
    except:
        pass