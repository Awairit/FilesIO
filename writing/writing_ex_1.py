# Writing the Data to the File
# To write the Data to the File, we have Two Pre-Defined Functions Present in File Pointer Object. They are
#     1. write()      --> Syntax:   FilePointerObj.write(str-data)                  ,If we have non-str Data then we convert the non-str data into str type data by using str()
#     2. writelines() --> Syntax:   FilePointerObj.writelines(Iterable-Object Data) ,If we have non-str Data then we convert the non-str data into str type data by using str()


Creator = "Guido Van Rossum"
with open("index.txt","w") as fp:
    print(f"The File Name  i.e. ({fp.name}) is present") #We cant ask to show the name of file by reference pointer variable name of file because its in try block if its in except block we can say it NameError
    fp.write("\t\t\tThe father of Python is {}\n".format(Creator))
    fp.write("Python")
    fp.write("\n\tChapters")

#=======================================================================================================================

with open("index.txt","a") as fp:
    fp.write("\nDjango")

#=======================================================================================================================

DOB= str(20021991) #Cant use other dataTypes other than 'str'
with open("index.txt","a") as fp:
    fp.write("\n Date of Official Release of Python is: {}" .format(DOB))

#======================================================================================================================

#Program for Writing the data to the Fite
#FiLeWriteEx1. PY
sno=300
sname="Rashed"
marks=23.451 # here snot sname and marks are called Objects resides in Main Memory.
with open("index.txt","a") as fp:
    fp.write("\n"+str(sno) + " \t ")
    fp.write(sname + " \t ")
    fp.write(str(marks) + " \t ")
