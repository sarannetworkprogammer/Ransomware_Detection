import ctypes

# Load the kernel32 library
kernel32 = ctypes.WinDLL("kernel32")

# Get a handle to the GetTickCount64 function
GetTickCount64 = kernel32.GetTickCount64
GetTickCount64.restype = ctypes.c_ulonglong

# Call GetTickCount64

tick_count = GetTickCount64()

# Print the tick count

print("Tick count:", tick_count)
