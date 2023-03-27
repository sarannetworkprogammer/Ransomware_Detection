#checking getversion api is called or not
# checking which process get_version api

import ctypes
import psutil
import os
import logging

# implementing logging functionality

# file opening for write the process 



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




if __name__  =="__main__":
    log_module()
    check_version()


