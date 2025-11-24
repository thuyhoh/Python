import os

path1 = "E:\\python\\text.txt"

if  os.path.exists(path1):
    print("that location exists!")
    if os.path.isfile(path1):     # check path1 is a file (files)
        print("that is a file")   # check path1 is link to director (foldeer,...)
    elif os.path.isdir(path1):
        print("that is a directory")
else:
    print("that location dosen't exist!")
