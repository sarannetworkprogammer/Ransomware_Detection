import psutil
import win32api
import win32process
import ctypes

PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010

def find_processes_with_ntqueryvaluekey():
    # Get the process ID for all running processes
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Open the process with PROCESS_QUERY_INFORMATION and PROCESS_VM_READ access
            hProcess = win32api.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, proc.pid)

            # Query the process memory to get the address of NtQueryValueKey
            base_addr = ctypes.c_void_p()
            size = ctypes.c_size_t()
            psutil.proc_memory_info(hProcess).get_ext_memory_regions()
            for region in psutil.proc_memory_info(hProcess).get_ext_memory_regions():
                if 'ntdll' in region.path.lower():
                    base_addr.value = region.addr
                    size.value = region.size
                    break

            if not base_addr:
                continue

            ntdll_dll = ctypes.WinDLL('ntdll', handle=base_addr)

            LdrGetProcedureAddress = ntdll_dll.LdrGetProcedureAddress
            LdrGetProcedureAddress.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p)]
            LdrGetProcedureAddress.restype = ctypes.c_int

            NtQueryValueKey_addr = ctypes.c_void_p()
            status = LdrGetProcedureAddress(base_addr, b'NtQueryValueKey', 0, ctypes.byref(NtQueryValueKey_addr))

            # If NtQueryValueKey is found in the process memory, check if the process has called it
            if NtQueryValueKey_addr:
                process_has_called_ntqueryvaluekey = False
                for thread in proc.threads():
                    try:
                        context = win32process.GetThreadContext(win32api.OpenThread(win32api.THREAD_ALL_ACCESS, False, thread.id))
                        instr_ptr = context.Eip
                        if instr_ptr >= NtQueryValueKey_addr.value and instr_ptr < NtQueryValueKey_addr.value + 20:
                            process_has_called_ntqueryvaluekey = True
                            break
                    except:
                        continue

                if process_has_called_ntqueryvaluekey:
                    print("Process {0} ({1}) has made an API call to NtQueryValueKey".format(proc.name(), proc.pid))

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass