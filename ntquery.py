import ctypes
import sys

# Define a structure for PROCESS_BASIC_INFORMATION
class PROCESS_BASIC_INFORMATION(ctypes.Structure):
    _fields_ = [("Reserved1", ctypes.c_void_p),
                ("PebBaseAddress", ctypes.c_void_p),
                ("Reserved2", ctypes.c_void_p * 2),
                ("UniqueProcessId", ctypes.c_ulong),
                ("Reserved3", ctypes.c_void_p)]

# Load the ntdll library
ntdll = ctypes.WinDLL("ntdll")

# Get a handle to the NtQueryInformationProcess function
NtQueryInformationProcess = ntdll.NtQueryInformationProcess
NtQueryInformationProcess.restype = ctypes.c_long

# Define some constants
ProcessBasicInformation = 0

# Call NtQueryInformationProcess
process_info = PROCESS_BASIC_INFORMATION()
process_handle = ctypes.c_void_p()
status = NtQueryInformationProcess(process_handle, ProcessBasicInformation, ctypes.byref(process_info), ctypes.sizeof(PROCESS_BASIC_INFORMATION), None)

if status != 0:
    print("NtQueryInformationProcess failed with status code", status)
    sys.exit(1)

# Print the process information
print("Process ID:", process_info.UniqueProcessId)
print("PEB Base Address:", process_info.PebBaseAddress)