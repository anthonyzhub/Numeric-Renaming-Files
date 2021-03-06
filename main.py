#! /usr/bin/python3
import os
import sys
import re
import time
import stat

def getNewName():

    # OBJECTIVE: Request new file name from user

    while True:

        # Get input from user
        newName = input("Enter new name with '#': ")
        counter = input("Enter starting value: ")  

        if ("#" in newName) and counter.isnumeric():
            return (newName, int(counter))

"""
def getAllFiles(directoryPath):

    # OBJECTIVE: Return a sorted list of all non-hidden files inside directory

    # Create a list
    filesList = list()

    # Iterate dictionary's contents
    for f in os.listdir(directoryPath):

        # Create string of file's full path
        pathName = directoryPath + f

        # If item is not a directory and is not hidden, then add to list
        if os.path.isfile(pathName) and re.match('[^.]', f):
            filesList.append(pathName)

    # Return sorted list
    # filesList.sort()
    return filesList
"""

def getAllFiles(path):

    sortedDict = dict()

    # Add full path to list
    entryPaths = [os.path.join(path, file) for file in os.listdir(path)]

    # Create a list of tuples that has statuses of each file
    fileStatuses = list()
    for filepath in entryPaths:
        fileStatuses.append((os.stat(filepath), filepath))
    # print(fileStatuses)

    # Collect date and file name
    files = list()
    for status, filepath in fileStatuses:
        if stat.S_ISREG(status[stat.ST_MODE]):
            files.append((status[stat.ST_CTIME], filepath))
    # print(files)

    for creationTime, filePath in sorted(files):

        creationDate = time.ctime(creationTime)
        fileName = os.path.basename(filePath)
        # sortedList.append(creationDate + " " + fileName)
        sortedDict[fileName] = creationDate

    # Sort dictionary based on values
    newDict = dict()
    for k, v in sorted(sortedDict.items(), key=lambda value: value[1]):
        newDict[k] = v
        print(k)

    return newDict

def doesFileExist(filesList):

    # OBJECTIVE: Check if file inside of list exists. If not, return False

    # Return false if list is empty
    if filesList == None:
        return False

    filesList.sort()

    # Iterate list
    for i in range(len(filesList)):

        # Pop if element doesn't exist
        if not os.path.exists(filesList[i]):
            filesList.pop(i)

        # Pop if element is a directory
        elif os.path.isdir(filesList[i]):
            filesList.pop(i)

    return filesList

def doesDirectoryExist(directoryPath):
    return os.path.exists(directoryPath) and os.path.isdir(directoryPath)

def renameAllFiles(pathName):

    # OBJECTIVE: Rename all files inside directory

    def helper(pathName, newName, counter):

        # Create an oldCounter for future use
        oldCounter = 0

        # Create a proposed/temporary name
        tmpName = pathName + newName.replace("#", "{}".format(counter))

        while True:

            # If file already exists, increment counter and copy its old value
            if os.path.exists(tmpName):

                oldCounter = counter
                counter += 1

            # If not, then return proposed name
            else:
                return (tmpName, counter)

            # Create another proposed/temporary name
            tmpName = pathName + newName.replace("#", "{}".format(counter))

    # Does path exist
    if doesDirectoryExist(pathName) == False:
        print("Invalid directory!")
        return

    # print(pathName)

    # Get all files inside directory
    filesList = getAllFiles(pathName)
    print(filesList)

    # Get new name
    newName, counter = getNewName()

    for f in filesList:

        # Create a temporary name
        # tmpName = pathName + newName.replace("#", "{}".format(counter))
        tmpName, counter = helper(pathName, newName, counter)

        # Rename file in OS
        print("Renaming {} to {}".format(f, tmpName))
        os.rename(f, tmpName)
        counter += 1

    # Print directory's contents
    printWorkingDirectory(pathName)

def renameSomeFiles(filesList):

    # OBJECTIVE: Rename selected files only

    # Get proposed name and counter
    newName, counter = getNewName()

    # Iterate list
    for f in filesList:

        # Create a temporary name
        tmpName = newName.replace("#", "{}".format(counter))

        # Rename file
        os.system("mv {} {}".format(f, tmpName))
        counter += 1

    # Print directory's contents
    printWorkingDirectory(getWorkingDirectory())

def getWorkingDirectory():
    return os.getcwd()

def printWorkingDirectory(pathName):
    os.system("ls -l {}".format(pathName))

if __name__ == "__main__":

    """ OPTIONS:
    -a => all files
    -s <file names> => some files
    -h => help
    """

    # Turn sys.argv into a list
    cmds = sys.argv

    if "-h" in cmds:
        print("How-To:")
        print("Rename all files inside the directory with './main.py -a <path>'")
        print("Rename some files inside the directory with './main.py -s <files>'")
        exit()

    if "-a" in cmds and "-s" in cmds:
        print("ERROR: Only select one option!")
        exit()

    if "-a" in cmds:

        # Slice list to get directory's path
        filePath = cmds[-1]

        # If filePath is ".", then request current working directory
        if filePath == ".":
            filePath = getWorkingDirectory()

        # NOTE: If path doesn't end with /, then directory cannot be accessed
        if filePath[-1] != "/":
            filePath += "/"
        
        renameAllFiles(filePath)

    if "-s" in cmds:

        # Slice list to get all files
        filesList = cmds[2:]

        # Check if every file exists
        filesList = doesFileExist(filesList)
        # print(filesList)

        # NOTE: This means user didn't pass either a directory or files don't exist
        if filesList == False or len(filesList) == 0:
            print("ERROR: Either directory was entered or files don't exist")
            exit()

        # Pass list to function for renaming
        renameSomeFiles(filesList)