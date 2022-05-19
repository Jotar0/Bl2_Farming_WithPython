import glob
import time
import win32api
import os
from stat import S_IREAD,S_IWUSR

print("READ ONLY FARMING BORDERLANDS !!\n")

bool_1 = True
dir_name = r'C:\Users\asus\Documents\My Games\Borderlands 2\WillowGame\SaveData\76561198065997643/'
# Get list of all files only in the given directory
list_of_files = filter( os.path.isfile,
                        glob.glob(dir_name + '*') )
# Sort list of files based on last modification time in ascending order
list_of_files = sorted( list_of_files,
                        key = os.path.getmtime)
# Iterate over sorted list of files and print file path
# along with last modification time of file
for file_path in list_of_files:
    timestamp_str = time.strftime(  '%d/%m/%Y :: %H:%M:%S',
                                time.gmtime(os.path.getmtime(file_path)))
    print(timestamp_str, ' -->', file_path)
files = os.listdir(dir_name)

for f in files:
	print(f)

aux = input("Introduceti ce save file vreti sa folositi:")
print("Pentru a inchide executabilul apasati 0 \n")
print("Pentru a face fisierul read only apasati 9 \n")

while True:
    a = win32api.GetKeyState(0x39)
    c = win32api.GetKeyState(0x30)

    if a < 0:
        os.chmod(r"C:\Users\asus\Documents\My Games\Borderlands 2\WillowGame\SaveData\76561198065997643"+str(aux),S_IREAD)
        while bool_1 == True:
            print("READ ONLY STATE")
            bool_1 = False
    if c<0:
        os.chmod(r"C:\Users\asus\Documents\My Games\Borderlands 2\WillowGame\SaveData\76561198065997643" + str(aux),S_IWUSR)
        print("Exiting application,Reverting changes to file..")
        time.sleep(3)
        break