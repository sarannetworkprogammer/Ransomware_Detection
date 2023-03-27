import psutil
import ctypes


def check_ntopen():

    def get_process_by_pid(pid):
        """Get process information by PID."""
        process = None
        for proc in psutil.process_iter():
            try:
                if pid == proc.pid:
                    process = proc
                    break
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return process

    def get_process_by_ntopenkey(handle):
        """Get process information for process that triggered NtOpenKey function."""
        pid = ctypes.windll.kernel32.GetCurrentProcessId()
        process = get_process_by_pid(pid)
        return process

    def nt_open():
        """Main function to demonstrate usage."""
        # Get the process information for the process that triggered NtOpenKey function
        handle = ctypes.windll.kernel32.GetCurrentProcess()
        process = get_process_by_ntopenkey(handle)
        
        # Print the process information
        if process:
            print("Process Name:", process.name())
            print("Process ID:", process.pid)
        else:
            print("Process not found.")

if __name__ == '__main__':
    main()