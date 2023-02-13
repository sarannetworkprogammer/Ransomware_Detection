import ctypes

def is_debugger_present():
    # Load the kernel32 library
    kernel32 = ctypes.windll.kernel32

    # Call the IsDebuggerPresent function
    result = kernel32.IsDebuggerPresent()

    # Return True if a debugger is present, False otherwise
    return result != 0

# Get the process ID of the current process
pid = ctypes.windll.kernel32.GetCurrentProcessId()

# Check if a debugger is present
debugger_present = is_debugger_present()

# Print the result
if debugger_present:
    print("Process {0} is being debugged".format(pid))
else:
    print("Process {0} is not being debugged".format(pid))