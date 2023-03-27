# Not working some error os exceptions



import psutil

import ctypes

# Load the ntdll library
ntdll = ctypes.WinDLL('ntdll')

# Get the handle to ntdll.dll
kernel32 = ctypes.WinDLL('kernel32')
GetModuleHandle = kernel32.GetModuleHandleW
GetModuleHandle.restype = ctypes.c_void_p
ntdll_handle = GetModuleHandle('ntdll.dll')

# Get the address of LdrGetProcedureAddress
LdrGetProcedureAddress_addr = ctypes.c_void_p()
LdrGetProcedureAddress_addr.value = kernel32.GetProcAddress(ctypes.c_size_t(ntdll_handle), b'LdrGetProcedureAddress')

# Define the arguments and return type of LdrGetProcedureAddress
argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
LdrGetProcedureAddress = ctypes.WINFUNCTYPE(ctypes.c_int, *argtypes)

# Call LdrGetProcedureAddress
dll_handle = ctypes.c_void_p()
function_name = ctypes.c_char_p(b'NtClose')
ctypes.windll.ntdll.LdrGetProcedureAddress(ntdll_handle, function_name, 0, ctypes.byref(dll_handle))

# Enumerate all running processes on the system
for process in psutil.process_iter():
    try:
        # Open the process for reading memory
        process_handle = ctypes.windll.kernel32.OpenProcess(0x10, False, process.pid)

        # Read the memory of the process to look for LdrGetProcedureAddress
        module_handles = psutil.Process(process.pid).memory_maps()
        for module_handle in module_handles:
            base_address = module_handle.addr
            module_size = module_handle.rss
            module_data = ctypes.create_string_buffer(module_size)

            # Read the memory of the process
            bytes_read = ctypes.c_size_t()
            ctypes.windll.kernel32.ReadProcessMemory(process_handle, base_address, module_data, module_size, ctypes.byref(bytes_read))

            # Check if LdrGetProcedureAddress is called in the memory
            function_address = ctypes.c_void_p()
            while True:
                function_address = ctypes.c_void_p(ctypes.c_char.from_buffer(module_data).find(ctypes.c_char.from_buffer(LdrGetProcedureAddress_addr), function_address.value))
                if function_address.value == 0:
                    break

                # We found an instance of LdrGetProcedureAddress being called!
                print(f"Process {process.name()} (pid {process.pid}) is calling LdrGetProcedureAddress at address 0x{function_address.value:x} in module {module_handle.path}")

    except (psutil.AccessDenied, psutil.NoSuchProcess, WindowsError):
        pass









