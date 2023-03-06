import wmi

c = wmi.WMI()

for process in c.Win32_Process():
    
    modules = process.modules
    for module in modules:
        if module.Name == "kernel32.dll":
            if "GetTickCount64" in module.Export:
                print(f"Process {process.ProcessId} ({process.Name}) called GetTickCount64()")
   