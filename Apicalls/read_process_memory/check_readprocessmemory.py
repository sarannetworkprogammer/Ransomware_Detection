# code not working some errors

import ctypes
import psutil

PROCESS_ALL_ACCESS = 0x1F0FFF
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

# Load the process identifier of the process calling the API
process_id = psutil.Process().pid

# Open the current process with PROCESS_ALL_ACCESS permissions
process_handle = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, process_id)

kernel32_handle = ctypes.windll.kernel32.LoadLibraryA("kernel32.dll")

# Get the address of the ReadProcessMemory function in kernel32.dll
read_process_memory_addr = ctypes.windll.kernel32.GetProcAddress(kernel32_handle, b'ReadProcessMemory', ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)))






# Define the signature of the ReadProcessMemory function
kernel32.ReadProcessMemory.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)]
kernel32.ReadProcessMemory.restype = ctypes.c_bool

# Create a ctypes buffer to hold the data read from the process's memory
buffer_size = 1024
read_buffer = ctypes.create_string_buffer(buffer_size)

# Call the ReadProcessMemory function to read a portion of the process's memory
result = kernel32.ReadProcessMemory(process_handle, ctypes.c_void_p(0x7ffd0de9aa20), ctypes.byref(read_buffer), ctypes.sizeof(read_buffer), None)

# Get the process name of the process calling the API
process_name = psutil.Process(process_id).name()

# Print the process name if the API was successfully called
if result:
    print(f"Process {process_name} called ReadProcessMemory.")
else:
    print("Failed to call ReadProcessMemory.")