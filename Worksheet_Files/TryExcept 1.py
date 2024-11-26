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
- Modify the function file writer
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

