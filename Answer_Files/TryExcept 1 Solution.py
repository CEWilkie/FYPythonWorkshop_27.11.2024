"""
                        PART ONE
"""

def ReadFile(filePath):
    fileLines = []

    try:
        # open the file and read contents
        file = open(filePath)

        fileLines = file.readlines()

        file.close()
    except:
        # OSError, the file path was bad
        print("File not found")
    else:
        # Everything was ok!
        print("No issues occurred")

    return fileLines

# Expects that "File not found" is printed
ReadFile("This Path Doesnt Work")


"""
                        PART TWO
"""


def Divide(numerator, denominator):
    try:
        # assumes that both values are ints, and denominator is non-0
        result = numerator / denominator

    except TypeError:
        print("Only Numbers can be used")

    except ZeroDivisionError:
        print("Cannot divide by 0")

    else:
        # instruction only called when no errors occur
        print("The result is: " + str(result))

Divide("a", 2)  # outputs: "Only Numbers can be used"
Divide(17, 0)  # outputs: "Cannot divide by 0"
Divide(6, 4)  # outputs: "The result is: 1.5"



"""
                        PART THREE
"""


def WriteNumberToFile(filePath):
    addedNumbers = []

    try:
        # read mode is necessary to prevent creation of unwanted files from bad filepath
        file = open(filePath, 'r')
        file.close()

        # now actually open the file as wanted
        file = open(filePath, 'a')

        while True:
            usrNum = input("Enter a number to add to the file, or 'eof'' to stop writing numbers: ")
            if usrNum == "eof":
                break

            # Add inputted number to list. Attempting to convert non-numeric throws ValueError
            addedNumbers.append(int(usrNum))

            # assuming nothing went wrong, this writes the original input string and a comma separator
            file.write(usrNum + ",")

        # normal operations, file closes here
        file.close()

    except OSError:
        # file.close() does not need to be done as it is never assigned
        print("File not found!")

    except ValueError:
        print("Non-Integer entered")
        # file.close() is required as the function is now exited before the normal operations file.close()
        file.close()

    finally:
        # this always outputs no matter the results of the function
        print("added numbers: " + str(addedNumbers))


WriteNumberToFile("Numbers.txt")
WriteNumberToFile("../ImportFiles/Numbers.txt")