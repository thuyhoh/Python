try:

    with open('test.txt',"r") as file: # open file
        print(file.read())         # read  file
        print("file name: ",file.name)
        print("file mode",file.mode)

except FileNotFoundError:
    print("that file was not found :(")
except FileExistsError:
    print("that file was not exist")


    