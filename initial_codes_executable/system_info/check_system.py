import ctypes
import psutil


def check_systeminfo():

    # Define the API function we want to detect
    kernel32 = ctypes.WinDLL("kernel32.dll")
    GetSystemInfo = kernel32.GetSystemInfo
    GetSystemInfo.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
    GetSystemInfo.restype = None

    count = 0
    # Iterate through the running processes
    for proc in psutil.process_iter():
        try:
            sys_info = ctypes.c_void_p()
            GetSystemInfo(ctypes.byref(sys_info))
            if sys_info.value:
                print("Process '{}' has called the GetSystemInfo API".format(proc.name()))
                count = count + 1
        except:
            pass
    print(f"Total number of process called ={count}")

if __name__ =="__main__":
    check_systeminfo()