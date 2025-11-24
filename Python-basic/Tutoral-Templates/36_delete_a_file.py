# import xlsxwrter
import os
import shutil
path = input("enter your file/folder that you want to delete")

try:
    os.remove(path)     # remove a file    
    #  os.rmdir(path)      # remove a folder
    #  shutil.rmtree(path) # remove folder and all files within folder
except FileNotFoundError:
    print("that file is not found")
except PermissionError:
    print("you do not have permission to delete that")
else:
    print(path + " was deleted")