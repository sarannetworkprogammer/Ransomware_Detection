import ctypes

def query_information_process(process_handle, process_information_class):
    # Define a structure to store the result of the NtQueryInformationProcess call
    class PROCESS_BASIC_INFORMATION(ctypes.Structure):
        _fields_ = [
            ("Reserved1", ctypes.c_void_p),
            ("PebBaseAddress", ctypes.c_void_p),
            ("Reserved2", ctypes.c_void_p * 2),
            ("UniqueProcessId", ctypes.c_ulong),
            ("Reserved3", ctypes.c_void_p)
        ]

    process_information = PROCESS_BASIC_INFORMATION()
    return_length = ctypes.c_ulong()

    # Load the ntdll library
    ntdll = ctypes.windll.ntdll

    # Call the NtQueryInformationProcess function
    result = ntdll.NtQueryInformationProcess(
        process_handle,
        process_information_class,
        ctypes.byref(process_information),
        ctypes.sizeof(process_information),
        ctypes.byref(return_length)
    )

    # Return the result of the NtQueryInformationProcess call
    return result, process_information

# Get the handle of the current process
process_handle = ctypes.windll.kernel32.GetCurrentProcess()

# Call the NtQueryInformationProcess function to retrieve information about the current process
result, process_information = query_information_process(process_handle, 0)

# Check the result of the NtQueryInformationProcess call
if result == 0:
    print("NtQueryInformationProcess call was successful")
    print("UniqueProcessId: {0}".format(process_information.UniqueProcessId))
else:
    print("NtQueryInformationProcess call failed")

# Close the handle to the current process
ctypes.windll.kernel32.CloseHandle(process_handle)