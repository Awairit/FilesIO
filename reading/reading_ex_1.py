#program for Reading the Data from File.
#FileReadEx1.py
try:
    with open("D:\\Python\\FilesIO\\writing\\index.txt","r") as fp:
        filedata=fp.read()                                     #--> Uses 'read'
        print("--------------------------------")
        print(filedata)
        print("--------------------------------")
except FileNotFoundError:
    print("File Does not Exist")

#=======================================================================================================================

# FileReadEx2.py
try:
    with open("D:\\Python\\FilesIO\\writing\\index.txt", "r") as fp:
        filedata = fp.readlines()                   # Uses 'readlines'
        print("--------------------------------")
        print(filedata)
        print("--------------------------------")
except FileNotFoundError:
    print("File Does not Exist")

#=======================================================================================================================

# FileReadEx1.py
try:
    with open("D:\\Python\\FilesIO\\writing\\index.txt", "r") as fp:
        filedata = fp.read()                     #Uses 'readlines' and uses loop
        print("--------------------------------")
        for i in filedata:
            print(i,end="")
        print("--------------------------------")
except FileNotFoundError:
    print("File Does not Exist")