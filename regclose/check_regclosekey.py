import psutil
import win32api
import win32process
import ctypes

PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010

def find_processes_with_regclosekey():
    # Get the process ID for all running processes
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Open the process with PROCESS_QUERY_INFORMATION and PROCESS_VM_READ access
            hProcess = win32api.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, proc.pid)

            # Query the process memory to get the address of RegCloseKey
            base_addr = ctypes.c_void_p()
            size = ctypes.c_size_t()
            psutil.proc_memory_info(hProcess).get_ext_memory_regions()
            for region in psutil.proc_memory_info(hProcess).get_ext_memory_regions():
                if 'advapi32' in region.path.lower():
                    base_addr.value = region.addr
                    size.value = region.size
                    break

            if not base_addr:
                continue

            advapi32_dll = ctypes.WinDLL('advapi32', handle=base_addr)

            RegCloseKey_addr = ctypes.c_void_p()
            RegCloseKey_addr.value = advapi32_dll.RegCloseKey

            # If RegCloseKey is found in the process memory, check if the process has called it
            if RegCloseKey_addr:
                process_has_called_regclosekey = False
                for thread in proc.threads():
                    try:
                        context = win32process.GetThreadContext(win32api.OpenThread(win32api.THREAD_ALL_ACCESS, False, thread.id))
                        instr_ptr = context.Eip
                        if instr_ptr >= RegCloseKey_addr.value and instr_ptr < RegCloseKey_addr.value + 20:
                            process_has_called_regclosekey = True
                            break
                    except:
                        continue

                if process_has_called_regclosekey:
                    print("Process {0} ({1}) has made an API call to RegCloseKey".format(proc.name(), proc.pid))

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass