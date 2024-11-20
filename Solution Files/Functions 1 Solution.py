
"""
                        PART ONE
"""

def GetMenuSelection(menuOptions, inputPrompt):
    for option in menuOptions:
        print(option)

    userInput = input(inputPrompt)

    return userInput




def Calculator():
    firstValue = int(input("first value: "))

    print("Select from the following")
    userSelection = GetMenuSelection(["add", "subtract", "multiply", "divide"],
                                      "select mode [1 - 4]:")
    userSelection = int(userSelection)

    secondValue = int(input("second value: "))

    calcResult = 0
    if userSelection == 1:
        calcResult = firstValue + secondValue

    elif userSelection == 2:
        calcResult = firstValue - secondValue

    elif userSelection == 3:
        calcResult = firstValue * secondValue

    elif userSelection == 4:
        calcResult = firstValue / secondValue

    return calcResult





useCalc = 0
while useCalc != 2:
    print("welcome to calculator program")

    result = Calculator()

    print("result = " + str(result))

    print("Would you like to use the calculator again?")
    userSelection = GetMenuSelection(["yes", "no"],
                                     "select yes/no [1 - 2]:")

    useCalc = int(userSelection)










"""
                        PART TWO
"""


def GetMenuSelection(menuTitle, menuOptions, inputPrompt):
    print(menuTitle)

    index = 1
    for option in menuOptions:
        print(str(index) + ": " + option)
        index += 1

    userInput = input(inputPrompt)

    return userInput

# or, if you wanted to get fancy with the enumerate() function
def GetMenuSelectionEnumerated(menuTitle, menuOptions, inputPrompt):
    print(menuTitle)

    for index, option in enumerate(menuOptions, 1):
        print(str(index) + ": " + option)

    userInput = input(inputPrompt)

    return userInput



def Calculator():
    firstValue = int(input("first value: "))

    userSelection = GetMenuSelection(
        "Select method of operation:",
        ["add", "subtract", "multiply", "divide"],
        "select mode [1 - 4]:")

    userSelection = int(userSelection)

    secondValue = int(input("second value: "))

    calcResult = 0
    if userSelection == 1:
        calcResult = firstValue + secondValue

    elif userSelection == 2:
        calcResult = firstValue - secondValue

    elif userSelection == 3:
        calcResult = firstValue * secondValue

    elif userSelection == 4:
        calcResult = firstValue / secondValue

    return calcResult





useCalc = 0
while useCalc != 2:
    print("welcome to calculator program")

    result = Calculator()

    print("result = " + str(result))

    userSelection = GetMenuSelection(
        "Would you like to use the calculator again?",
        ["yes", "no"],
        "select yes/no [1 - 2]:")

    useCalc = int(userSelection)


"""
                        PART THREE
"""

def GetMenuSelection(menuTitle, menuOptions, inputPrompt):
    print(menuTitle)

    index = 1
    for option in menuOptions:
        print(str(index) + ": " + option)
        index += 1

    userInput = int(input(inputPrompt))

    while userInput < 1 or userInput > len(menuOptions):
        print("Invalid Selection Please Try Again")
        userInput = int(input(inputPrompt))

    return userInput


def Calculator():
    firstValue = int(input("first value: "))

    userSelection = GetMenuSelection(
        "Select method of operation:",
        ["add", "subtract", "multiply", "divide"],
        "select mode [1 - 4]:")

    secondValue = int(input("second value: "))

    calcResult = 0
    if userSelection == 1:
        calcResult = firstValue + secondValue

    elif userSelection == 2:
        calcResult = firstValue - secondValue

    elif userSelection == 3:
        calcResult = firstValue * secondValue

    elif userSelection == 4:
        calcResult = firstValue / secondValue

    return calcResult





useCalc = 0
while useCalc != 2:
    print("welcome to calculator program")

    result = Calculator()

    print("result = " + str(result))

    useCalc = GetMenuSelection(
        "Would you like to use the calculator again?",
        ["yes", "no"],
        "select yes/no [1 - 2]:")
