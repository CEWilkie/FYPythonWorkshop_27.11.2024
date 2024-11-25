"""
Creating Loops

For this exercise, we will cover For Loops (range-based, item-based, enumerated) and while loops
This will also incorporate the usage of break, continue, conditional if/else


Suggested Material:
"A Guide To Loops"


                PART ONE
- Create a loop to print out all values stored in fileLines to the terminal


                PART TWO
- Create a loop which will split up a sentence into a list of individual words
- The loop should exit early if the word "close" is ever detected, not storing "close" or any words after it
- Output all the words which were detected before close (and not including close)

Suggested Material:
using String's .split(' ') to get individual words from the sentence
https://www.w3schools.com/python/ref_string_split.asp


                PART THREE
- Loop over a 2D Array of `SimpleClass` objects:
    - Output the key value 'Name'
    - Call their function `ReadyToDisplay()`. If this is true, call their function `DisplayInformation()`
      otherwise, skip on to the next class





"""

# fileLines is a list of lines read from a file

fileLines = open('../ImportFiles/BasicTextFile1.txt').readlines()
maxLines = len(fileLines)

# Loop to read through the lines:





# simple sentence of multiple words

sentence = "Howdy hey and good afternoon, have you seen how close it is to the Christmas break now?"
wordsList = []

# Loop to get each word from sentence before close










import random

# Dont worry about this class, you wont need to change anything in it for this section

class SimpleClass() :
    name = "_unsetName"
    number = random.randint(0, 50)
    readyToDisplay = False
    def __init__(self, name, displayable = False):
        self.name = name
        self.readyToDisplay = displayable

    def ReadyToDisplay(self):
        return self.readyToDisplay

    def DisplayInformation(self):
        print(f"Hello! My name is {self.name}")


objects = [["Object 1", SimpleClass("My Object 1", True)],
           ["Object 2", SimpleClass("Another Object", True)],
           ["Object 3", SimpleClass("This Object should not display")],
           ["Object 4", SimpleClass("Final Object", True)]]


# Loop over all objects for output




