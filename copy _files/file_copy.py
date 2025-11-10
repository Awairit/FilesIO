#Write a Python Program which will copy the content of One File into another File.
#FileCopyEx.py
def filecopy():
    try:
        srcfile=input("Enter Source File Name:")
        with open(srcfile,"r") as rp: # Opened the Source File in Read Mode
            destfile=input("Enter Destination File:")
            with open(destfile,"a") as wp: # Opened the Dest File in write Mode
                #read the Data from Source File
                srcfiledata=rp.read()
                #Write the srcfiledata to the Destination file
                wp.write(srcfiledata)
                print("Source File Data copied into Destnation file")
    except FileNotFoundError:
        print("Source File Does not Exist")
#Main Program
filecopy() # Function Call