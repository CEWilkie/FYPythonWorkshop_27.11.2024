

"""
                        PART ONE
"""

fileLines = open('../Test/BasicTextFile1.txt').readlines()
maxLines = len(fileLines)

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


for word in sentence.split(' '):
    if word == "close":
        break

    else:
        wordsList.append(word)

for word in wordsList:
    print(word)






