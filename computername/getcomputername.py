

import ctypes

# Call GetComputerName to get the computer name
computer_name = ctypes.create_string_buffer(256)
size = ctypes.c_size_t(256)
if ctypes.windll.kernel32.GetComputerNameA(computer_name, ctypes.byref(size)) == 0:
    print(f"Error: {ctypes.WinError()}")
else:
    print(f"Computer name: {computer_name.value.decode('utf-8')}")
