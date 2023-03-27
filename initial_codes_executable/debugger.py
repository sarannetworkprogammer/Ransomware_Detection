import ctypes
import sys
def debugger():
# Load the kernel32 library
    kernel32 = ctypes.WinDLL("kernel32")

    # Get a handle to the IsDebuggerPresent function
    IsDebuggerPresent = kernel32.IsDebuggerPresent
    IsDebuggerPresent.restype = ctypes.c_bool

    # Call IsDebuggerPresent
    if IsDebuggerPresent():
        print("A debugger is attached to the process.")
    else:
        print("No debugger is attached to the process.")