"""
                        PART ONE
"""

# if the file cannot be found, just change this path to make it work for you :>
FileReadWriteTest_path = "../ImportFiles/FileReadWriteTest.txt"


# Open up the file, whilst mode "r" (read) can be specified as in the second variation shown,
# it is also the default mode and so is not required, hence the following two commands are the same
file = open(FileReadWriteTest_path)
file = open(FileReadWriteTest_path, "r")

for line in file.readlines():
    print(line, end="") # `end=""` drops the newline character for more compact print. This isnt necessary

# Close the file when done
file.close()


"""
                        PART TWO
"""

# retrieve mode "w" for write, or "a" for append from user input
openType = input("Select File Write Mode: [a] append to end, or [w] to write from start: ")

# Add in a check to ensure that the openType is valid
# defaults to "w" if not
if openType != "w" and openType != "a":
    openType = "w"

# Open the file
file = open(FileReadWriteTest_path, openType)

# while the user has not entered eof, take the users input and add it to the end of the file

while True:
    newLine = input("Write line to file: ")
    if (newLine == "eof"):
        # exit the loop!
        break

    else:
        # use an additional newline character to make sure that lines are separated in the file
        file.write(newLine + "\n")

# Close the file
file.close()

"""
    PART TWO ALTERNATIVE
"""

# Retrieve all the lines from the user and then append them at once

lines = []
while True:
    line = input("Write line to file: ")
    if line == "eof":
        # stop fetching more lines
        break

    else:
        # use an additional newline character to make sure that lines are separated in the file
        lines.append(line + "\n")

# retrieve mode "w" for write, or "a" for append from user input
openType = input("Select File Write Mode: [a] append to end, or [w] to write from start: ")

# Add in a check to ensure that the openType is valid
# defaults to "w" if not
if openType != "w" and openType != "a":
    openType = "w"

# Open the file
file = open(FileReadWriteTest_path, openType)

file.writelines(lines)
file.close()


"""
    PART TWO ALTERNATIVE
"""

# retrieve mode "w" for write, or "a" for append from user input
openType = input("Select File Write Mode: [a] append to end, or [w] to write from start: ")

# Add in a check to ensure that the openType is valid
# defaults to "w" if not
if openType != "w" and openType != "a":
    openType = "w"

# Open the file
file = open(FileReadWriteTest_path, openType)

# Or alternatively, if you wanna get cool in Python 3.8 try this assignment expression while loop
# instead of `while True:` newLine is assigned, and checked simultaneously that it is not eof

while (newLine := input("Write line to file: ")) != "eof":
    file.write(newLine + "\n")

file.close()


"""
                        PART THREE
"""

# Function to fix file data separators
def FixFileSeparators(filePath, currentDataSeparator):
    # Read lines from file, returns list of strings.
    # .close() does not need to be called as the file is not stored open, but immediately read
    fileLines = open(filePath, "r").readlines()

    # split the data using currentDataSeparator
    fileLinesFixed = []

    for line in fileLines:
        # strip then split the line
        lineData = line.split(currentDataSeparator)

        # now merge the line data
        fixedLine = ""
        for data in lineData:
            # this also adds a comma to the end of the line
            fixedLine += data + ","

        # so we remove the final comma here by taking a substring from start to end-1
        fixedLine = fixedLine[:-1]
        # or do: fixedLine = fixedLine.removesuffix(',')

        # Now add the line to fixedLines
        fileLinesFixed.append(fixedLine)

    # Write the fixed lines to the file
    file = open(filePath, "w")
    for line in fileLinesFixed:
        # why might we not need to add in a newline for this?
        file.write(line)

    file.close()


# File to fix
fileToFixPath = "../ImportFiles/FixingFileDataSeparators.txt"

# pass to function with separator ":::"
FixFileSeparators(fileToFixPath, ":::")
