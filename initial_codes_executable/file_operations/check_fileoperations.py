import psutil

#This code takes longer time

def check_process_file_operations():
    count = 0
    # Get the list of process IDs using the psutil library
    process_ids = psutil.pids()

    # Loop through the list of process IDs
    for pid in process_ids:
        try:
            process = psutil.Process(pid)

            # Get the process name and executable path
            process_name = process.name()
            process_exe = process.exe()

            # Get the list of open files for the process
            open_files = process.open_files()

            # Check if the process has any open files
            if len(open_files) > 0:
                print("Process ID:", pid)
                count = count +1
                
            
                #print("Process name:", process_name)
                #print("Process executable:", process_exe)
                #print("Open files:")

                # Loop through the list of open files and print the file paths
                #for file in open_files:
                    #print("\t", file.path)
        except:
            pass
        
    return count

# Call the check_process_file_operations function
count = check_process_file_operations()

print(f"Total no_of files_opend ={count}")