import psutil

for proc in psutil.process_iter(['pid', 'name']):

    try:
        # Get the list of open handles for the process
        handles = proc.open_files()
        
        # Check if any of the handles match the "GetComputerNameA" API
        for handle in handles:
            if "GetComputerNameA" in handle.path:
                print(f"Process {proc.pid} ({proc.name()}) called the GetComputerNameA API.")
                break
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        pass

    