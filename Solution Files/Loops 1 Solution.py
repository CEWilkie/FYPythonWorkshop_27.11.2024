import random


"""
                        PART ONE
"""

# Just fetches all lines from the file for example data
fileLines = open('../ImportFiles/BasicTextFile1.txt').readlines()
maxLines = len(fileLines)

# takes each line in the list of lines and prints it
for line in fileLines:
    print(line, end="")

for line in range(maxLines):
    print(fileLines[line], end="")

# Either of those above two solutions are valid, but the first is a bit of a more suitable method
# end="" is completely optional! It just removes the additional newline that print
# gives to the line, making the text more compact. Pretty cool huh?



"""
                        PART TWO
"""


sentence = "Howdy hey and good afternoon, have you seen how close it is to the Christmas break now?"
wordsList = []

# sentence.split(' ') splits the single string into a list of strings, separated by the space character
for word in sentence.split(' '):

    # Exit early using break
    if word == "close":
        break

    # Add the word into the list
    else:
        wordsList.append(word)

# print out all the words in the list
for word in wordsList:
    print(word)



"""
                        PART THREE
"""

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

for obj in objects:
    print(obj[0] + ": ")

    if not obj[1].ReadyToDisplay():
        print()  # add in an extra newline
        continue

    obj[1].DisplayInformation()
    print() # add in an extra newline