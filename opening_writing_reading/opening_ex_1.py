#File Modes r, w, a, r+, w+, a+, x, x+
#open files by two methods
# 1. 'open("fileName", "fileMode")' Need to close opened file by filePointer.close(), --> syntax: variable_name=open("fileName", "fileMode")
# 2. 'with open("fileName", "fileMode") as :' no need to close PVM will close as lines of code get out from indentation block, --> syntax:  with open("fileName", "fileMode") as variable_name:

try:
    fp = open("student.txt","r") #if file is not present we cant read it that's why it gives "FileNotFoundError"
except FileNotFoundError:
    print("File not found, please check the path or File Does not Exist")
else:
    print("File opened successfully") #if 'try:' block works 'else' block works
    print('Is file closed or not', fp.closed)
finally:
    try:
        fp.close()
        print('Is file closed or not', fp.closed)
        print("File closed successfully")
    except NameError: #we don't have file so it can't assign it to a variable i.e. Name
        print("File Name Itself does not opened-there is no need to close:")

#=======================================================================================================================

#program for Demonstrating Opening the File
#FileOpenEx1.py
try:
    fp=open("kvr1.data","r")
except FileNotFoundError:
    print("File Does not Exist")
else:
    print("--------else block-------------")
    print("File Opened in read Mode")
    print("Type of fp=", type(fp))
    print("else block:Is File Closed?:",fp.closed)
    print("-------------------------------")
finally:
    print("I am from Finally Block")
    try:
        fp.close() # Relinquish the Resource--Manually closing
        print("finally block:Is File Closed?:", fp.closed)
    except NameError:
        print("File Name Itself does not opened-there is no need to close:")


# Mode,| First Line:                               |   Action & Pointer Position,                             |  Second Line:                                 |   File Creation & Overwrite Behavior                               |
# -----|-------------------------------------------|----------------------------------------------------------|-----------------------------------------------|--------------------------------------------------------------------|
# r,   | Read mode;                                |   pointer starts at the beginning of the file.,          |  Requires the file to exist;                  |   raises FileNotFoundError if it doesn't.                          |
# w,   | Write mode;                               |   pointer starts at the beginning of the file.,          |  Creates the file if it doesn't exist;        |   overwrites content if it does.                                   |
# a,   | Append mode;                              |   pointer starts at the end of the file.,                |  Creates the file if it doesn't exist;        |   appends to existing content if it does.                          |
# r+,  | Read and Write mode;                      |   pointer starts at the beginning of the file.,          |  Requires the file to exist;                  |   allows both reading and writing (overwriting current content).   |
# w+,  | Write and Read mode;                      |   pointer starts at the beginning of the file.,          |  Creates the file if it doesn't exist;        |   overwrites content if it does.                                   |
# a+,  | Append and Read mode;                     |   pointer starts at the end of the file for writing.,    |  Creates the file if it doesn't exist;        |   allows reading from the start and writing at the end.            |
# x,   | Exclusive Creation mode;                  |   pointer starts at the beginning of the file.,          |  Creates the file only if it does not exist;  |   raises FileExistsError otherwise.                                |
# x+,  | Exclusive Creation and Read/Write mode;   |   pointer starts at the beginning of the file.,          |  Creates the file only if it does not exist;  |   raises FileExistsError otherwise.                                |

#=======================================================================================================================

#program for Demonstrating Opening the File
#FileOpenEx2.py
fp=open("sample.txt","w")
print("File Created and Opened in Write Mode")
print("Type of fp=",type(fp))  # <class '_io.TextIOWrapper'>

#=======================================================================================================================

#program for Demonstrating Opening the File
#FileOpen(with open('file_name','File Mode') as file_pointer_variable:) Ex1.py
try:
    with open("kvr2.data","r") as fp:
        print("--------with open() as-------------")
        print("\tFile Opened in read Mode")
        print("\tType of fp=", type(fp))
        print("\twith open() as: Is File Closed?:", fp.closed)
        print("-------------------------------------")
    print("--------after with open() as-------------")
    print("\tafter with open() as: Is File Closed?:", fp.closed)
except FileNotFoundError:
    print("File Does not Exist")

#=======================================================================================================================

#program for Demonstrating Opening the File along with File attributes
#FileOpenEx4.py
try:
    with open("kvr2.data","a+") as fp:
        print("----------------------------------------")
        print("\twith open() as: Is File Closed?:", fp.closed)
        print("\tFile Name:{}".format(fp.name))
        print("\tFile Opening Mode:{}".format(fp.mode))
        print("\tIs File Readable? :{}".format(fp.readable()))
        print("\tIs File Writable? :{}".format(fp.writable()))
        print("-----------------------------------------")
    print("--------after with open() as-------------")
    print("\tafter with open() as: Is File Closed?:", fp.closed)
except FileNotFoundError:
    print("File Does not Exist")