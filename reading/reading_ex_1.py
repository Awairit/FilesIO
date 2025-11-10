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

# FileReadEx3.py
try:
    with open("D:\\Python\\FilesIO\\writing\\index.txt", "r") as fp:
        filedata = fp.read()                     #Uses 'readlines' and uses loop
        print("--------------------------------")
        for i in filedata:
            print(i,end="")
        print("--------------------------------")
except FileNotFoundError:
    print("File Does not Exist")

#=======================================================================================================================

#Write a Python Program which will read any file name and display Its Content.
#FileReadEx3.py
try:
    filename=input("Enter Any File Name:")
    with open(filename,"rt") as fp:
        filedata=fp.read()
        print("-------------------------------------")
        print(filedata)
        print("-------------------------------------")
except FileNotFoundError:
    print("File Does not Exist")

#=======================================================================================================================

