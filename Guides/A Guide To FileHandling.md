# FileHandling

#### [Return to Contents](../README.md)

Additional Materials found at:
<br> [Python File Handling - w3schools](https://www.w3schools.com/python/python_file_handling.asp)
<br> [CSVs with Pandas Library - w3schools](https://www.w3schools.com/python/pandas/default.asp)

### What is Filehandling in Python?

Typically you will have managed files directly through the file explorer, however Python 
is also fully capable of interacting with files. This may be deleting, creating, writing
to and reading from.

This guide will cover specifically the inbuilt `open()` file manager within python, and
parsing CSVs and their data.

##
### In-Built File Handling

Python comes ready with its own set of functions for managing and utilising files. The 
primary methods that you are likely to work with will be `open()`, `close()`, `write()`, 
`read()` and `readlines()`, however I encourage you to check documentation on other key 
methods of the filehandling system via the linked resources at the top

#### Opening and Closing files

The typical syntax for opening a file involves either assigning a file object using 
solely open(), or alternatively immediately reading all lines from a file object and 
storing those. File objects require additional care as they should be closed when no
longer in use to prevent issues such as attempting to open a file which is still open,
or not properly updating a file with its changes.

Example with utilising a file object:

```python
# opening a new file object
file = open("../ImportFiles/FileReadWriteTest.txt")

for line in file.readlines():
    print(line, end="")

# same output result
print(file.read())

# close the file
file.close()
```

Example where the file lines are directly read from the file without needing to manage
the file object

```python
# notice the immediate call for .readlines() ?
fileLines = open("../ImportFiles/FileReadWriteTest.txt").readlines()

for line in fileLines:
    print(line, end="")

# same output result
fileString = open("../ImportFiles/FileReadWriteTest.txt").read()
print(fileString)
```

Below will be some further information on how to properly use the necessary functions for
effective file management.

#### Open, FilePaths and Mode

- Open

`open()` takes a filePath parameter and an optional mode parameter. The filepath directs
the function to a file to open. The mode is used to specify if the file should be opened
under either `read`, `write` or `append` (these are the most common ones you will use. 
There are an additional 4). These modes will be further elaborated on in the "Mode" section.

- Paths

the `open()` function's only required parameter is a file path. This path may be absolute
or relative (path from the project root / origin). In code in this repository, often
I have appended `../` to the start of a file path. Since I program in Pycharm, relative
paths originate from the current file. Hence I need to back out of the current file's 
folder in order to access a file / folder not in the current directory. 

With visual studio, relative paths always originate from the project root folder.
This means that the prefix of `../` is not necessary, and instead the path can immediately
specify a directory (or further).

```python
# exit the `Guides` directory, enter the `ImportFiles` directory and 
# then file `ReadWriteTest`
myFile = open("../ImportFiles/FileReadWriteTest.txt")
myFile.close()

# Visual Studio alternative
myFile = open("ImportFiles/FileReadWriteTest.txt")
myFile.close()
```

If you encounter issues running the program, make sure that file paths are set correct for
your environment!

- Mode

The secondary, optional, parameter of `open()` is the mode. As mentioned, this involves 
opening the file in either `read`, `write` or `append` via passing `"r"`, `"w"`, or 
`"a"` to the parameter. The parameter is by default set to `"rt"` for read text (this is
equivalent to mode `"r"`, the `"t"` simply specifies more precisely to use text mode). These modes
also indicate what functionality is available to the file object, and hence the 
restrictions applied to it. Attempting to use restricted functions on the file object
will result in an UnsupportedOperation error being thrown.

Files opened in read mode cannot have new content written to them. They are purely for
retrieving contents of the specified file.

Files opened in write or append mode cannot read contents of the file.

Another mode you may find useful is `"x"` or `create` This will create a new file and
return a writeable file object if the file does not exist. However, it will cause an error
if the file does already exist.

- Nifty Tricks You May Like

An alternative method that you may find useful, when you wish to utilise a file object
but prevent yourself from worrying about proper closure of the file is to utilise
`with ... as:`. 

```python
with open("../ImportFiles/BasicTextFile1.txt") as myFile:
    for line in myFile.readlines():
        print(line, end="")

# with has exited, so myFile is automatically closed due to going out
# of scope
```

Additionally, you can utilise the mode `"r+"` to open the file in both read and append
mode. This is particularly useful when you are attempting to make a modification to a
particular line or lines of the file, and saves you having to reopen the file object.
The code below wishes to modify each line to add ":endline" to the end of it, so it
needs to read all the lines from the file in order to edit them

```python
with open("../ImportFiles/EditingFiles.txt", "r+") as myFile:
    fileLines = myFile.readlines()

    # enumerate required to modify the actual lines in fileLines
    for i, line in enumerate(fileLines, 0):
        # strip removes preceeding / trailing whitespace and newline 
        # characters
        cleanedLine = line.strip()
        fileLines[i] = cleanedLine + " :endline\n"

    # without this, .write() would apply to the end of the file. This
    # specifies the character from which the writer starts writing
    myFile.seek(0)

    for line in fileLines:
        myFile.write(line)

```

#### Read and Readlines

`read()` will return a singular string containing the full contents read from the file.
This function can only be called on files which are opened in read mode.

`readlines()`, however, will return a list of strings. Each string is a single line from the 
file. As with read, it can also only be called on files opened in read mode.

`readline()` will return the next line that can be read from the file. Once all lines have
been read from the file, `readline()` returns an empty string: `""`

#### Write and WriteLines

`write()` is used on a file opened with either append or write mode to write a string
to the file. When writing strings to a file, be aware that newline breaks are not 
automatically applied, meaning you will have to add `"\n"` into any position where a 
newline is desired. 

`writelines()` is capable of taking a list of strings to write to the file, performing
`.write()` for each of them.

##
### CSV and Excel File Handling with Pandas

Pandas is an external library that you would import into your python program through 
`import pandas as pd` (or you could use an alternative name for pandas rather than `pd`).
This library is not by default ready to use until being correctly imported and installed.
However, it can vastly improve your ability to parse CSV and Excel data sets.

It reads the files and produces a "DataFrame" object, which can provide easy interaction 
with and manipulation of the data within the python environment. Using the code below,
you can retrieve the average number of Sales and Visitors last week across all stores 
in the file `"StoreVisitorSalesData.csv"`

```python
import pandas as pd

storeProduce = pd.read_csv("../ImportFiles/StoreVisitorSalesData.csv")
print(storeProduce)
```

However, I will not go into too much information on this. Pandas Dataframes are particularly powerful tools which may
end up oversimplifying your coursework. I would suggest instead attempting to build up a parser for the csv files
yourself, which will easily help you implement classes and get used to utilising data and files.

For those of you interested still in Pandas, I would make sure that you do not let it prevent your own development.
Further reading material on it can be found [here](https://www.w3schools.com/python/pandas/default.asp) or you can
utilise the learning resource "Files 3 - CSVs with Pandas.py"



