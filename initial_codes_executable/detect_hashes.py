import psutil
import hashlib


# all the hases of Ransomware will be updated here this list will be pushed from the server 

def detect_ransomware():
    
    known_ransomware_hashes = {
        "2f9d0b907388cbc083656f1c8b7ebb13": "WannaCry",
        "3b9af200bfc075549af4a4fa7eea32c1": "Petya",
        "919a9c5a5e5f5c527b097a8c5a5b7d5c": "NotPetya"
    }


# This gives the process running in the system
    process_list = psutil.process_iter()

    for process in process_list:
        #print(process)
        try:
            process_exe = process.exe()
            #rb is binary mode which gives correct hash 

            with open(process_exe, "rb") as file:
                file_data = file.read()
                file_hash = hashlib.md5(file_data).hexdigest()
                if file_hash in known_ransomware_hashes:

                    return known_ransomware_hashes[file_hash]
        
        except (psutil.NoSuchProcess, psutil.NoSuchProcess, psutil.AccessDenied,FileNotFoundError):
            pass

        return None


if __name__ == "__main__":

    result = detect_ransomware()
    if result:
        print(f"Ransomware detected :{result}")
    else:
        print("No ransomwarre detected")

        


