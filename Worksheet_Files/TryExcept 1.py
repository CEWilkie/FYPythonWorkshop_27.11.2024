"""
TryExcept

For this exercise, we will utilise the try... except blocks to catch errors in order to retain smooth
program flow

Suggested Materials:
"A Guide To TryExcept"


                PART ONE
- Modify the function "ReadFile" to handle errors raised when a file cannot be found
- The function should print "File not found" when the file is not found
- The function should print "No issues occured" when no issues occur

                PART TWO
- Modify the function division, so that it prints "Only Numbers can be used" if one or both
values are not numbers
- Modify the function division so that it prints "Cannot divide by 0" if division by 0 is attempted
- The function should otherwise output the results of the division

you will need to catch exceptions TypeError and ZeroDivisionError separately


                PART THREE
- Modify the function 'WriteNumberToFile' so that when a non-integer is inputted that is not 'eof' it outputs
"Non-Integer entered"
- Ensure that this change does not prevent the function outputting "File not found!" when the file is not found
- Modify the function 'WriteNumberToFile' so that it utilises a finally to always output the numbers which have
been added to the file

"""


def ReadFile(filePath):
    file = open(filePath)
    fileLines = file.readlines()
    file.close()

    return fileLines

ReadFile("This Path Doesnt Work")




def Divide(numerator, denominator):
    result = numerator / denominator
    print("The result is: " + str(result))


Divide("a", 2)
Divide(0, 0)
Divide(6, 4)





def WriteNumberToFile(filePath):
    addedNumbers = []

    try:
        # read mode is necessary to prevent creation of unwanted files from bad filepath
        file = open(filePath, 'r')
        file.close()

        # now actually open the file as wanted
        file = open(filePath, 'a')

        while True:
            # Fetch user input
            usrNum = input("Enter a number to add to the file, or 'eof'' to stop writing numbers: ")
            if usrNum == "eof":
                break

            # Add inputted number to list
            addedNumbers.append(int(usrNum))

            # Write input to file
            file.write(usrNum + ",")

        # normal operations, file closes here
        file.close()

    except OSError:
        print("File not found!")



WriteNumberToFile("Numbers.txt")
WriteNumberToFile("../ImportFiles/Numbers.txt")