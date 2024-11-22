"""
Creating Functions

For this exercise lets turn a bunch of repeated code into a function

You are going to want to take the numerous print statements which make user menus
and turn them into a callable function. Menus are marked with comments signalling
the start and end of a menu


                PART ONE
- create the new function GetMenuSelection with parameters for the menu options and an input prompt.
- have it print each menu option to the terminal
- have it print the input prompt to terminal and return the user input

Suggested Material:
"A Guide To Functions"
"A Guide To Loops" or Loops 1.py


                PART TWO
- GetMenuSelection takes in another parameter for the menu title
- GetMenuSelection now prints each menu option with an incrementing index starting from 1 (options 1, 2, 3, 4, ...)

Suggested Material
"A Guide To Loops" or Loop Creation 1.py


                PART THREE
- GetMenuSelection will now ensure that the user enters a suitable input within the range of 1 to the max option index
- GetMenuSelection will now return an integer index value

(note that you do not need to worry about checking if the user input is a valid integer, thats covered in
"TryCatch 1")


                FINAL CHECKLIST

The function GetMenuSelection should have parameters to take in:
    - A Menu Title to be outputted
    - Menu Options to be outputted
    - A Prompt for the user to retrieve input

Additionally:
    - Options should have incrementing indexes starting from 1
    - Returns an index as inputted by the user (ie: 0, 1, 5, etc)
"""


# Define the Menu Function here
# def Menu()



# Simple Calculator Function

def Calculator():
    firstValue = int(input("first value: "))

    # Menu
    print("Select from the following")
    print("add")
    print("subtract")
    print("multiply")
    print("divide")

    mode = int(input("select mode [1 - 4]:"))
    # End of menu

    secondValue = int(input("second value: "))

    calcResult = 0
    if (mode == 1):
        calcResult = firstValue + secondValue

    elif mode == 2:
        calcResult = firstValue - secondValue

    elif mode == 3:
        calcResult = firstValue * secondValue

    elif mode == 4:
        calcResult = firstValue / secondValue

    return calcResult




# Main Loop of program

useCalc = 0
while useCalc != 2:
    print("welcome to calculator program")

    # Calculator
    result = Calculator()
    print("result = " + str(result))
    #

    # Menu
    print("Would you like to use the calculator again?")
    print("Yes")
    print("No")

    userInput = int(input("select yes/no [1 - 2]:"))
    # End of Menu

    useCalc = userInput
