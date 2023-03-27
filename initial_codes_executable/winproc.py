import ctypes

# Define a function prototype for EnumProcesses
EnumProcessesProto = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_uint), ctypes.c_uint, ctypes.POINTER(ctypes.c_uint))

# Load the Psapi library
psapi = ctypes.WinDLL("psapi")

# Get a handle to the EnumProcesses function
EnumProcesses = EnumProcessesProto(("EnumProcesses", psapi))

# Call EnumProcesses
processes = (ctypes.c_uint * 1024)()
cb = ctypes.sizeof(processes)
bytes_returned = ctypes.c_uint()

EnumProcesses(processes, cb, ctypes.byref(bytes_returned))

# Print the process IDs
for i in range(bytes_returned.value // ctypes.sizeof(ctypes.c_uint)):
    print("Process ID:", processes[i])