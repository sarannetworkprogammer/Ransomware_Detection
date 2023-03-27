import win32api
import win32process

# Define a function to handle trace events
def handle_event(event):
    # Check if the event is a DeviceIoControl call
    if event[1] == 'DeviceIoControl':
        # Get the process ID and name from the event data
        process_id = event[0]
        process_name = win32process.GetModuleFileNameEx(win32api.OpenProcess(1040, False, process_id), 0)
        # Print the process name and ID
        print(f"Process {process_name} ({process_id}) called DeviceIoControl.")

# Start tracing system calls
win32api.SetConsoleCtrlHandler(lambda x: True, True)
win32api.SetConsoleTitle('Tracing System Calls...')
win32api.WinExec('cmd.exe /k "auditpol /set /subcategory:"Process Creation"" /success:enable /failure:enable"', 0)
win32api.WinExec('cmd.exe /k "logman create trace -n WinTrace -o WinTrace.etl -p {0x3e1aa16a-9f14-4c84-864f-4b23a0654de4} 0xffffffffffffffff -ets"', 0)
win32api.WinExec('cmd.exe /k "logman start WinTrace"', 0)
win32api.WinExec('cmd.exe /k "ping -n 10 127.0.0.1 > nul && tracerpt WinTrace.etl -of csv -o WinTrace.csv -y -ft"', 0)

# Read trace events and handle them
with open('WinTrace.csv', 'r') as f:
    for line in f:
        event = line.strip().split(',')
        handle_event(event)

# Stop tracing system calls
win32api.WinExec('cmd.exe /k "logman stop WinTrace -ets"', 0)