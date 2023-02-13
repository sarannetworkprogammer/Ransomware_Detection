# finding system details

import ctypes

# Define a structure for SYSTEM_INFO
class SYSTEM_INFO(ctypes.Structure):
    _fields_ = [("wProcessorArchitecture", ctypes.c_ushort),
                ("wReserved", ctypes.c_ushort),
                ("dwPageSize", ctypes.c_uint),
                ("lpMinimumApplicationAddress", ctypes.c_void_p),
                ("lpMaximumApplicationAddress", ctypes.c_void_p),
                ("dwActiveProcessorMask", ctypes.c_void_p),
                ("dwNumberOfProcessors", ctypes.c_uint),
                ("dwProcessorType", ctypes.c_uint),
                ("dwAllocationGranularity", ctypes.c_uint),
                ("wProcessorLevel", ctypes.c_ushort),
                ("wProcessorRevision", ctypes.c_ushort)]

# Load the kernel32 library
kernel32 = ctypes.WinDLL("kernel32")

# Get a handle to the GetSystemInfo function
GetSystemInfo = kernel32.GetSystemInfo
GetSystemInfo.restype = None

# Call GetSystemInfo
system_info = SYSTEM_INFO()
GetSystemInfo(ctypes.byref(system_info))

# Print the system information
print("Processor Architecture:", system_info.wProcessorArchitecture)
print("Number of Processors:", system_info.dwNumberOfProcessors)
print("Processor Type:", system_info.dwProcessorType)
print("Allocation Granularity:", system_info.dwAllocationGranularity)
print("Processor Level:", system_info.wProcessorLevel)
print("Processor Revision:", system_info.wProcessorRevision)