# solving error in main program

import ctypes

# Define the buffer size
size = ctypes.c_ulong(256)

print(f"size ={size.value}")

# Allocate a buffer to receive the computer name
computer_name = ctypes.create_unicode_buffer(size.value)

print(f"computer_name ={computer_name}")

# Call the GetComputerName function to retrieve the computer name
success = ctypes.windll.kernel32.GetComputerNameW(computer_name, ctypes.byref(size))

if success:
    print("Computer Name:", computer_name.value)
else:
    print("Failed to retrieve computer name")