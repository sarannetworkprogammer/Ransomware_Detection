import psutil


import ctypes

kernel32 = ctypes.WinDLL("kernel32.dll")


imGetVersion = kernel32.GetVersion
GetVersion.argtypes = []
GetVersion.restype = ctypes.c_ulong

for proc in psutil.process_iter():
    try:
        version = GetVersion()
        if version:
            print("Process '{}' has called the GetVersion API".format(proc.name()))
            #a = proc.name()
    except:
        pass


