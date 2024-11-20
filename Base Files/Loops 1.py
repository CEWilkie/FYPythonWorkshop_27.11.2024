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







"""

# fileLines is a list of lines read from a file

fileLines = open('../Test/BasicTextFile1.txt').readlines()
maxLines = len(fileLines)

# Loop to read through the lines:





# simple sentence of multiple words

sentence = "Howdy hey and good afternoon, have you seen how close it is to the Christmas break now?"
wordsList = []

# Loop to get each word from sentence before close
