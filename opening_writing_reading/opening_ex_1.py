#File Modes r, w, a, r+, w+, a+, x, x+
#open files by two methods
# 1. 'open("fileName", "fileMode")' Need to close opened file by filePointer.close(), --> syntax: variable_name=open("fileName", "fileMode")
# 2. 'with open("fileName", "fileMode") as :' no need to close PVM will close as lines of code get out from indentation block, --> syntax:  with open("fileName", "fileMode") as variable_name:

fp = open("student.txt","r") #if file is not present we cant read it that's why it gives "FileNotFoundError"