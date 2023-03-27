import ctypes
import psutil

def get_process_by_handle(handle):
    """Get process information by handle."""
    process = None
    for proc in psutil.process_iter():
        try:
            if handle == proc.handle():
                process = proc
                break
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return process

def get_process_by_device_control(device_handle, io_control_code):
    """Get process information for process that triggered DeviceIoControl function."""
    result = ctypes.windll.kernel32.DeviceIoControl(device_handle, io_control_code, None, 0, None, 0, ctypes.byref(ctypes.c_ulong()), None)
    if result == 0:
        return None
    handle = ctypes.windll.kernel32.GetCurrentProcess()
    process = get_process_by_handle(handle)
    return process

def main():
    """Main function to demonstrate usage."""
    # The device handle and IO control code parameters to be passed to DeviceIoControl function
    device_handle = 0
    io_control_code = 0
    
    # Get the process information for the process that triggered DeviceIoControl function
    process = get_process_by_device_control(device_handle, io_control_code)
    
    # Print the process information
    if process:
        print("Process Name:", process.name())
        print("Process ID:", process.pid)
    else:
        print("Process not found.")

if __name__ == '__main__':
    main()