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


