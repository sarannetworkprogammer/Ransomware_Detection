import win32api
import win32process

# Define a function to handle trace events
def handle_event(event):
    # Check if the event is an NtOpenDirectoryObject call
    if event[1] == 'NtOpenDirectoryObject':
        # Get the process ID and name from the event data
        process_id = event[0]
        process_name = win32process.GetModuleFileNameEx(win32api.OpenProcess(1040, False, process_id), 0)
        # Print the process name and ID
        print(f"Process {process_name} ({process_id}) called NtOpenDirectoryObject.")

# Start tracing system calls
win32api.SetConsoleCtrlHandler(lambda x: True, True)
win32api.SetConsoleTitle('Tracing System Calls...')
win32api.WinExec('cmd.exe /k "auditpol /set /subcategory:"Process Creation"" /success:enable /failure:enable"', 0)
win32api.WinExec('cmd.exe /k "logman create trace -n WinTrace -o WinTrace.etl -p {0x3e1aa16a-9f14-4c84-864f-4b23a0654de4} 0xffffffffffffffff -ets"', 0)
win32api.WinExec('cmd.exe /k "logman start WinTrace"', 0)
win32api.WinExec('cmd.exe /k "tracerpt WinTrace.etl -of csv -o WinTrace.csv -y -ft"', 0)

# Read trace events and handle them
with open('WinTrace.csv', 'r') as f:
    for line in f:
        event = line.strip().split(',')
        handle_event(event)

# Stop tracing system calls
win32api.WinExec('cmd.exe /k "logman stop WinTrace -ets"', 0)



"""


This script uses the win32api and win32process modules to start tracing system calls and handle trace events. It first sets up the tracing environment by enabling process creation auditing and creating a trace session. It then reads trace events from a CSV file and passes them to the handle_event function, which checks if the event is an NtOpenDirectoryObject call and prints a message indicating the name and PID of the process that made the call. Finally, the script stops the trace session.

Note that this approach requires elevated privileges and may not work on all systems. Additionally, tracing system calls can have a significant performance impact and may not be suitable for use in production environments.

"""


