
# This code check_version and check_sysem_info

import ctypes
import psutil
import os
import logging
import win32process


# implementing logging functionality

def log_module():

    logging.basicConfig(filename='version.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')



# kill process function
def kill_process(name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == name:
            pid_to_kill = proc.info['pid']
            try:
                os.kill(pid_to_kill, 9)
                print(f"Process with PID {pid_to_kill} killed successfully")
                logging.warning(f"this process killed sucessfully ={pid_to_kill}")
            except OSError as e:
                print(f"Error killing process with PID {pid_to_kill}: {e}")
                logging.warning(f"Error in kiling process ={pid_to_kill}")

###############################################################################################
def check_version():
    # Define the API function we want to detect
    
    file = open("version.txt", "w")
    kernel32 = ctypes.WinDLL("kernel32.dll")
    GetVersion = kernel32.GetVersion
    GetVersion.argtypes = []
    GetVersion.restype = ctypes.c_ulong
    count = 0
    all_count =0
    white_list = ['System Idle Process', 'System', '', 'Registry',  'csrss.exe', 'msedgewebview2.exe', 'wininit.exe', 'conhost.exe', 'services.exe', 'LsaIso.exe', 'lsass.exe', 'svchost.exe', 'fontdrvhost.exe', 'svchost.exe', 'svchost.exe', 'svchost.exe', 'HP.JumpStarts.exe', 'Code.exe', 'svchost.exe', 'Code.exe', 'svchost.exe', 'svchost.exe', 'svchost.exe', 'svchost.exe', 'MMSSHOST.exe', 'svchost.exe', 'svchost.exe', 'svchost.exe', 'slack.exe', 'svchost.exe', 'svchost.exe', 'ETDCtrl.exe', 'svchost.exe', 'svchost.exe', 'svchost.exe', 'svchost.exe', 'svchost.exe', 'RuntimeBroker.exe', 'svchost.exe', 'TextInputHost.exe', 'CiscoCollabHostCef.exe', 'AvastBrowser.exe', 'svchost.exe', 'svchost.exe', 'svchost.exe', 'AppHelperCap.exe', 'NetworkCap.exe', 'DiagsCap.exe', 'svchost.exe', 'SysInfoCap.exe', 'TouchpointAnalyticsClientService.exe', 'WUDFHost.exe', 'svchost.exe', 'svchost.exe', 'svchost.exe', 'svchost.exe', 'svchost.exe', 'svchost.exe', 'svchost.exe', 'amdfendrsr.exe', 'atiesrxx.exe', 'svchost.exe', 'svchost.exe', 'svchost.exe', 'svchost.exe', 'svchost.exe', 'dasHost.exe', 'svchost.exe', 'svchost.exe', 'dasHost.exe', 'svchost.exe', 'svchost.exe', 'wsc_proxy.exe', 'svchost.exe', 'svchost.exe', 'svchost.exe', 'conhost.exe', 'MemCompression', 'svchost.exe', 'AdobeCollabSync.exe', 'unsecapp.exe', 'dllhost.exe', 'McAMTaskAgent.exe', 'WmiPrvSE.exe', 'svchost.exe', 'StartMenuExperienceHost.exe', 'MfeAVSvc.exe', 'svchost.exe', 'nxclient.bin', 'svchost.exe', 'RuntimeBroker.exe', 'horizon_client_service.exe', 'svchost.exe', 'svchost.exe', 'svchost.exe', 'svchost.exe', 'Cortana.exe', 'svchost.exe', 'ETDService.exe', 'svchost.exe', 'AvastSvc.exe', 'AGMService.exe', 'DriverUpdSvc.exe', 'armsvc.exe', 'agent_ovpnconnect_1647517251935.exe', 'svchost.exe', 'AGSService.exe', 'TuneupSvc.exe', 'aswToolsSvc.exe', 'svchost.exe', 'spoolsv.exe', 'afwServ.exe', 'svchost.exe', 'msedgewebview2.exe', 'AvastBrowser.exe', 'OneDrive.exe', 'ftscanmgrhv.exe', 'mfemms.exe', 'ModuleCoreService.exe', 'mysqld.exe', 'nxservice64.exe', 'ovpnhelper_service.exe', 'msedgewebview2.exe', 'svchost.exe', 'PEFService.exe', 'RtkBtManServ.exe', 'TouchpointGpuInfo.exe', 'RtkAudUService64.exe', 'svchost.exe', 'VpnSvc.exe', 'nessus-service.exe', 'vmware-usbarbitrator64.exe', 'vmwsprrdpwks.exe', 'WebexHost.exe', 'SECOMN64.exe', 'WildTangentHelperService.exe', 'svchost.exe', 'nessusd.exe', 'VpnNM.exe', 'mysqld.exe', 'svchost.exe', 'ctfmon.exe', 'powershell.exe', 'conhost.exe', 'svchost.exe', 'svchost.exe', 'aswEngSrv.exe', 'AvastBrowser.exe', 'slack.exe', 'AvastBrowser.exe', 'mfevtps.exe', 'Code.exe', 'msedge.exe', 'ProtectedModuleHost.exe', 'Creative Cloud UI Helper.exe', 'AggregatorHost.exe', 'nxserver.bin', 'conhost.exe', 'QcShm.exe', 'svchost.exe', 'msedgewebview2.exe', 'HPSystemEventUtilityHost.exe', 'svchost.exe', 'chrome.exe', 'OneDrive.exe', 'RuntimeBroker.exe', 'svchost.exe', 'aswidsagent.exe', 'Adobe Desktop Service.exe', 'svchost.exe', 'svchost.exe', 'ModuleCoreService.exe', 'SearchHost.exe', 'conhost.exe', 'taskhostw.exe', 'node.exe', 'svchost.exe', 'svchost.exe', 'mcapexe.exe', 'AvastBrowser.exe', 'svchost.exe', 'Zoom.exe', 'svchost.exe', 'GoogleCrashHandler.exe', 'svchost.exe', 'McCSPServiceHost.exe', 'McUICnt.exe', 'CCLibrary.exe', 'AvastUI.exe', 'svchost.exe', 'taskhostw.exe', 'svchost.exe', 'Zoom.exe', 'svchost.exe', 'svchost.exe', 'Grammarly.Desktop.exe', 'nxd.exe', 'SgrmBroker.exe', 'CiscoCollabHostCef.exe', 'slack.exe', 'svchost.exe', 'winlogon.exe', 'GoogleCrashHandler64.exe', 'AvastBrowser.exe', 'svchost.exe', 'msedgewebview2.exe', 'mcshield.exe', 'svchost.exe', 'nxnode.bin', 'CiscoCollabHost.exe', 'chrome.exe', 'svchost.exe', 'AvastUI.exe', 'SecurityHealthService.exe', 'fontdrvhost.exe', 'svchost.exe', 'atmgr.exe', 'McPvTray.exe', 'HPCommRecovery.exe', 'conhost.exe', 'atieclxx.exe', 'chrome.exe', 'AppVShNotify.exe', 'slack.exe', 'msedgewebview2.exe', 'svchost.exe', 'ONENOTEM.EXE', 'msedge.exe', 'explorer.exe', 'svchost.exe', 'RuntimeBroker.exe', 'WhatsApp.exe', 'WmiPrvSE.exe', 'ShellExperienceHost.exe', 'backgroundTaskHost.exe', 'Code.exe', 'AdobeIPCBroker.exe', 'slack.exe', 'AvastBrowser.exe', 'McVulCtr.exe', 'cmd.exe', 'chrome.exe', 'notepad++.exe', 'OpenVPNConnect.exe', 'chrome.exe', 'RuntimeBroker.exe', 'mcafee-security-ft.exe', 'msedgewebview2.exe', 'HPAudioSwitch.exe', 'Creative Cloud UI Helper.exe', 'msedgewebview2.exe', 'SecurityHealthSystray.exe', 'svchost.exe', 'AvastBrowser.exe', 'msteams.exe', 'SystemSettingsBroker.exe', 'RuntimeBroker.exe', 'msedgewebview2.exe', 'slack.exe', 'chrome.exe', 'AvastBrowser.exe', 'dwm.exe', 'AvastUI.exe', 'taskhostw.exe', 'svchost.exe', 'svchost.exe', 'CoreSync.exe', 'AvastBrowser.exe', 'sihost.exe', 'RuntimeBroker.exe', 'Widgets.exe', 'msedgewebview2.exe', 'LockApp.exe', 'RuntimeBroker.exe', 'ModuleCoreService.exe', 'chrome.exe', 'Code.exe', 'svchost.exe', 'msedge.exe', 'RuntimeBroker.exe', 'RuntimeBroker.exe', 'RuntimeBroker.exe', 'python.exe', 'ai.exe', 'BridgeCommunication.exe', 'Code.exe', 'conhost.exe', 'csrss.exe', 'node.exe', 'msedge.exe', 'svchost.exe', 'svchost.exe', 'CCXProcess.exe', 'AdobeNotificationClient.exe', 'SearchProtocolHost.exe', 'conhost.exe', 'AvastBrowser.exe', 'OfficeClickToRun.exe', 'svchost.exe', 'chrome.exe', 'OpenVPNConnect.exe', 'RtkAudUService64.exe', 'AvastBrowser.exe', 'Microsoft.SharePoint.exe', 'msedge.exe', 'msedge.exe', 'svchost.exe', 'svchost.exe', 'conhost.exe', 'AvastBrowser.exe', 'OpenVPNConnect.exe', 'Code.exe', 'Code.exe', 'Code.exe', 'msedge.exe', 'OpenVPNConnect.exe', 'cmd.exe', 'svchost.exe', 'msedge.exe', 'msedgewebview2.exe', 'AvastUI.exe', 'chrome.exe', 'svchost.exe', 'AvastNM.exe', 'POWERPNT.EXE', 'BridgeCommunication.exe', 'msedgewebview2.exe', 'CastSrv.exe', 'chrome.exe', 'conhost.exe', 'msedge.exe', 'AdobeCollabSync.exe', 'AdobeUpdateService.exe', 'Creative Cloud.exe', 'chrome.exe', 'RuntimeBroker.exe', 'Code.exe', 'svchost.exe', 'mcafee-security.exe', 'msedge.exe', 'SearchIndexer.exe', 'svchost.exe']


    # Iterate through the running processes
    file.write("Listing the process which called get_version_api")
    for proc in psutil.process_iter():
        try:
            version = GetVersion()
            if version:
                #print("Process '{}' has called the GetVersion API".format(proc.name()))
                a = proc.name()
                
                logging.info(a)
                all_count = all_count + 1
                if a not in white_list:

                    file.write("\n")
                    file.write(a)
                    count = count + 1
                    b = kill_process(a)
                    

                
        except:
            pass

    



    print(f"process which are not whitlisted  ={count}")

    print(f"Total process which generated this api call  {str(all_count)}")
    file.write(f"\n Total process which generated this api call  {str(all_count)}")

    file.write(f"\n process which are not whitlisted {str(count)}")

    file.close()

#################################################################################################################
def check_systeminfo():

    # Define the API function we want to detect
    kernel32 = ctypes.WinDLL("kernel32.dll")
    GetSystemInfo = kernel32.GetSystemInfo
    GetSystemInfo.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
    GetSystemInfo.restype = None

    count = 0
    # Iterate through the running processes
    for proc in psutil.process_iter():
        try:
            sys_info = ctypes.c_void_p()
            GetSystemInfo(ctypes.byref(sys_info))
            if sys_info.value:
                print("Process '{}' has called the GetSystemInfo API".format(proc.name()))
                count = count + 1
        except:
            pass
 
    print(f"Total number of process called ={count}")

#####################################################################################################

def check_debugger():

    def is_debugger_present():
        # Load the kernel32 library
        kernel32 = ctypes.windll.kernel32

        # Call the IsDebuggerPresent function
        result = kernel32.IsDebuggerPresent()

        # Return True if a debugger is present, False otherwise
        return result != 0



    # Get the process ID of the current process
    pid = ctypes.windll.kernel32.GetCurrentProcessId()

    # Check if a debugger is present
    debugger_present = is_debugger_present()

    # Print the result
    if debugger_present:
        print("Process {0} is being debugged".format(pid))
    else:
        print("Process {0} is not being debugged".format(pid))


########################################################################

def check_process_enum_processes():
    # Get the list of process IDs using the psutil library
    process_ids = psutil.pids()

    # Loop through the list of process IDs
    for pid in process_ids:
        try:
            process = psutil.Process(pid)

            # Get the process name and executable path
            process_name = process.name()
            process_exe = process.exe()

            # Check if the process name or executable path contains the word "enum"
            if "enum" in process_name.lower() or "enum" in process_exe.lower():
                print("Process ID:", pid)
                print("Process name:", process_name)
                print("Process executable:", process_exe)
        except:
            pass

#####################################################################################
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
    
    nt_open()

############################################################################

def find_processes_with_create_snapshot():
    # Constants for CreateToolhelp32Snapshot function
    TH32CS_SNAPPROCESS = 0x00000002
    # Iterate over all running processes
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Open the process with PROCESS_QUERY_INFORMATION and PROCESS_VM_READ access
            hProcess = win32process.OpenProcess(win32process.PROCESS_QUERY_INFORMATION | win32process.PROCESS_VM_READ, False, proc.pid)

            # Get the module handle for kernel32.dll
            kernel32_handle = ctypes.windll.kernel32.GetModuleHandleA(b"kernel32.dll")

            # Get the address of CreateToolhelp32Snapshot
            CreateToolhelp32Snapshot_addr = ctypes.windll.kernel32.GetProcAddress(kernel32_handle, b"CreateToolhelp32Snapshot")

            # If CreateToolhelp32Snapshot is found in the process memory, check if the process has called it
            if CreateToolhelp32Snapshot_addr:
                process_has_called_create_snapshot = False
                for thread in proc.threads():
                    try:
                        context = win32process.GetThreadContext(win32process.OpenThread(win32process.THREAD_ALL_ACCESS, False, thread.id))
                        instr_ptr = context.Eip
                        if instr_ptr >= CreateToolhelp32Snapshot_addr and instr_ptr < CreateToolhelp32Snapshot_addr + 20:
                            process_has_called_create_snapshot = True
                            break
                    except:
                        continue

                if process_has_called_create_snapshot:
                    print("Process {0} ({1}) has made an API call to CreateToolhelp32Snapshot".format(proc.name(), proc.pid))

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass



######################################################################################





def check_all_apis():

    # here i will keep continous loop at the end i.e while true condition
   
    log_module()
    check_version()
    check_systeminfo()
    check_debugger()
    check_process_enum_processes()
    check_ntopen()
    find_processes_with_create_snapshot()






if __name__ == "__main__":
    check_all_apis()