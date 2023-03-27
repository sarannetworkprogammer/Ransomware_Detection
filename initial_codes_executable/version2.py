# give the opeerating system details

import ctypes
import sys

# Define a structure for OSVERSIONINFOEX
class OSVERSIONINFOEX(ctypes.Structure):
    _fields_ = [("dwOSVersionInfoSize", ctypes.c_ulong),
                ("dwMajorVersion", ctypes.c_ulong),
                ("dwMinorVersion", ctypes.c_ulong),
                ("dwBuildNumber", ctypes.c_ulong),
                ("dwPlatformId", ctypes.c_ulong),
                ("szCSDVersion", ctypes.c_wchar * 128),
                ("wServicePackMajor", ctypes.c_ushort),
                ("wServicePackMinor", ctypes.c_ushort),
                ("wSuiteMask", ctypes.c_ushort),
                ("wProductType", ctypes.c_byte),
                ("wReserved", ctypes.c_byte)]

# Load the kernel32 library
kernel32 = ctypes.WinDLL("kernel32")

# Get a handle to the GetVersionEx function
GetVersionEx = kernel32.GetVersionExW
GetVersionEx.restype = ctypes.c_bool

# Call GetVersionEx
os_version = OSVERSIONINFOEX()
os_version.dwOSVersionInfoSize = ctypes.sizeof(OSVERSIONINFOEX)

if not GetVersionEx(ctypes.byref(os_version)):
    print("GetVersionEx failed.")
    sys.exit(1)

# Print the version information
print("Windows version:", os_version.dwMajorVersion, ".", os_version.dwMinorVersion)
print("Build number:", os_version.dwBuildNumber)
print("Service Pack:", os_version.wServicePackMajor, ".", os_version.wServicePackMinor)