import ctypes
import psutil

# Define constants and types needed for GetComputerNameA function
MAX_COMPUTERNAME_LENGTH = 15
computer_name = ctypes.create_string_buffer(MAX_COMPUTERNAME_LENGTH + 1)
size = ctypes.c_ulong(MAX_COMPUTERNAME_LENGTH + 1)

# Get handle to kernel32.dll and the address of GetComputerNameA
kernel32_handle = ctypes.windll.kernel32.GetModuleHandleA('kernel32')
get_computer_name_addr = ctypes.windll.kernel32.GetProcAddress(kernel32_handle, 'GetComputerNameA')

# Create a function prototype to represent the signature of GetComputerNameA
GetComputerNameProto = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_char_p, ctypes.POINTER(ctypes.c_ulong))

# Cast the address of GetComputerNameA to the correct function prototype
GetComputerName = GetComputerNameProto(get_computer_name_addr)

# Call the GetComputerNameA function
GetComputerName(computer_name, ctypes.byref(size))

# Get the list of running processes on the system
for proc in psutil.process_iter(['pid', 'name', 'exe']):
    try:
        # Check if the process has called GetComputerNameA
        if 'GetComputerNameA' in proc.memory_maps()[0].path:
            print(f"Process {proc.name()} (pid {proc.pid}) called GetComputerNameA")
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        pass



        