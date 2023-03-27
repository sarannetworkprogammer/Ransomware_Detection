
# This code is perfectly working to kill the process

import psutil

# Define the process name to kill
process_name = "Notepad.exe"

# Find the process ID (PID) of the process by name
for proc in psutil.process_iter(['pid', 'name']):
    if proc.info['name'] == process_name:
        pid = proc.info['pid']
        print(f"Found {process_name} with PID {pid}")
        break
else:
    print(f"No process found with name {process_name}")
    exit()

# Kill the process by PID
try:
    process = psutil.Process(pid)
    process.terminate()
    print(f"{process_name} with PID {pid} has been terminated")
except psutil.NoSuchProcess:
    print(f"No process found with PID {pid}")