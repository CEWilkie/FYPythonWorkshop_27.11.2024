"""
Creating Loops

For this exercise, the basics of reading from and writing to standard txt files will be covered


Suggested Material:
"A Guide To Files"


                PART ONE
- Open and read the contents of `FileReadWriteTest.txt`

Suggested Material:
"A Guide To Loops"


                PART TWO
- Allow the user to write text to the file `FileReadWriteTest.txt`
- If the user inputs "eof" then stop writing to the file
- Allow the user to choose between appending to the end of the file or overwriting it from the start

Suggested Material:
"A Guide To Loops" and Loops 1
Remember "a" is to append, "w" is to write, "r" is to read


                PART THREE
- Using file `FixingFileDataSeparators.txt`
- Create a function with parameters for a file path and separator string
- Read the file contents using .split() so that it correctly reads the data separated by " ::: "
- Have the data written back into the file using separator ","
  such that data is written: DataElement1,DataElement2

Suggested Material:
"A Guide To Functions"
"""


# I suggest using a variable to store the file path like this. This can make things quicker to edit
# should the file path need changing!
FileReadWriteTest_path = "../ImportFiles/FileReadWriteTest.txt"
FixingFileSeparators_path = "../ImportFiles/FixingFileDataSeparators.txt"




