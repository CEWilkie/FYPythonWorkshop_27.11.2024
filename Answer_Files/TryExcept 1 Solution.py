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
                        PART TWO
"""


def WriteNumberToFile(filePath):
    try:
        # could cause an error from bad filepath
        file = open(filePath, "a")

        while True:
            usrNum = input("Enter a number to add to the file, or 'eof'' to stop writing numbers")
            if usrNum == "eof":
                break

            # Check is a number, could cause an error from being a non-numeric.
            int(usrNum)

            # assuming nothing went wrong, this writes the original input string and a comma separator
            file.write(usrNum + ",")


    except OSError:
        print("File not found!")

    except TypeError:
        print("Non-Integer entered")

    finally:
        file.close()

WriteNumberToFile("shdfbsdofjisdnfjksjdfnjkd")