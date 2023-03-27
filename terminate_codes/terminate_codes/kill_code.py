import os

# replace "pid_to_kill" with the PID of the process you want to kill
pid_to_kill = 12345

try:
    os.kill(pid_to_kill, 9)
    print(f"Process with PID {pid_to_kill} killed successfully")

except OSError as e:
    print(f"Error killing process with PID {pid_to_kill}: {e}")