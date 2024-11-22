# Functions

#### [Return to Contents](../README.md)

Additional Materials found at:
<br>[Python Functions - GeeksForGeeks](https://www.geeksforgeeks.org/python-functions/?ref=outind)
<br>[Python Functions - w3schools](https://www.w3schools.com/python/python_functions.asp)

### What are they?

Functions are a set of instructions executed whenever the function name is called. 
These instructions may include acting or utilising some given parameters in the function,
such as a String of text, or int number. Additionally, they may provide a return value
that can then be further used.

```python
# valid example of a simple function:

# define function
def Add(a, b):
    return a + b
    
# call function
result = Add(5, 6)
```

##
### Creating Functions

Function creation can be broken down into a few major components:
- Name
- Parameters
- Instructions
- Return Value

However, when making a function the only 100% required components is a Name and some 
Instructions to be carried out. The example function shown below has no parameters or
return value, only an instruction and name.

```python
def HelloWorld():
    print("Hello World!")

HelloWorld()
```

But such cases are unlikely due to being restrictive in capabilities, and so primarily
you are going to be using all components of functions! But lets get into a bit more 
detail on these components

#### Naming Functions

Function names need to be unique! So they cannot be the same as anything else within
the current scope (more on this in Advanced Python Info). For now, concern yourself 
with only the current file you are working in. Shown below are two functions, different
in all aspects except name:

```python
# Define function Add
def Add(a, b):
    return a + b

# Redefining function Add!
def Add(a, b, c):
    print(f"result of {a} + {b} + {c} = {a+b+c}")
```

Despite the second definition of `Add` taking a different number of parameters, doing a 
different instruction (print) and having no return value, the name is the same, and so it 
overwrites the first definition of `Add`!

```python
# This is now ok

def Add(a, b):
    return a + b

def PrintAddThree(a, b, c):
    print(f"result of {a} + {b} + {c} = {a+b+c}")
```

I also suggest making sure that your function names and parameter names give the program
user some insight into what they are doing. This would also benefit yourself if you ever
take a break from a project for a while, and can quickly remind yourself what does what.

#### Parameters

Parameters are the second key part of a function, acting as inputs which the function can
operate on. Shown in the previous examples was parameters _a, _b, and _c. These all 
represent some numbers that have been given to the function to add up. For more complex
functions, I would suggest utilising more suitable parameter names to more readily
identify what is what:

```python
def InsertIntoDatabase(dataBase, recordList):
    for record in recordList:
        freeIndex = len(dataBase)
        dataBase.loc[freeIndex] = record
```

Here, dataBase and recordList both clearly set out what is expected to be passed to 
the function, and should work towards minimising errors when debugging or using the
function.

Default values can also be set for parameters, using an assignment:
```python
def GetMenuSelection(menuOptions = None, inputPrompt = "Enter Input: "):
    if menuOptions is None:
        menuOptions = ["Yes", "No"]
    
    print("::: User Menu :::")
    for option in menuOptions:
        # prints out option 
        print("- " + option)
        
    # get input
    return input(inputPrompt)

GetMenuSelection(inputPrompt="Please Enter an Input:")
```

Default parameters allow the function to not require explicitly set parameters when calling,
but are overwritten whenever the parameter is specified. It is important to note that any 
parameter with a default argument must come at the end of the list of parameters, as any
parameter after that must also have a default argument. The example below would hence be invalid:

```python
def GetMenuSelection(menuOptions = None, inputPrompt):
    if menuOptions is None:
        menuOptions = ["Yes", "No"]
    
    print("::: User Menu :::")
    for option in menuOptions:
        # prints out option 
        print("- " + option)
        
    # get input
    return input(inputPrompt)

GetMenuSelection(inputPrompt="Please Enter an Input:")
```

As for why `= None` is being used here instead of assigning to the list, well its best 
I let you read up on it through [this StackOverflow post](https://stackoverflow.com/questions/41686829/why-does-pycharm-warn-about-mutable-default-arguments-how-can-i-work-around-the)
but dont worry about it too much. It just might explain some odd behaviour you see around 
though!

#### Instructions

Not much to say about this. These are just what is done by the function. Make sure
they are clear and understandable to make for easier debugging!

#### Return Value

Functions having return values just means you need to take a little extra care to make
sure you store or utilise their outputs properly:

```python
def Add(a, b):
    return a+b

# stored correctly for later use
result = Add(5, 6) 

# return value is lost
Add(7, 11)
```

##
### Using Functions Properly

Functions should be defined before any usages within code, otherwise python wont know
what the function being called is supposed to do. Typically this will be highlighted 
with a helpful error message to let you know.

```python
# invalid code:

# call function
result = Add(5, 6)

# define function
def Add(a, b):
    return a + b 
```

Additionally, make sure that all *required* parameters of a function are being 
passed to it correctly. Here both _a and _b are required values, with no preset defaults. 
Hence they are both required, else the program will fail.

```python
def Add(a, b):
    return a + b 

result = Add(5)
```

Also, when looking to create functions, you are looking to break up and modularise
sections of the program. Take for instance a case where you have a bunch of repeated
copy-pasted complex code thats used multiple times in a program. Should it turn out
that the code actually has a bug, that could result in you having to fix multiple separate
instances of the same code. Instead you can have a singular function - meaning that a bug
in the function only needs to be fixed once! 

```python
# first input

print("::: User Menu :::")
options = ["Option 1", "Option 2"]
for option in options:
    # prints out option 
    print("- " + option)
resultOne = input("selection: ")

# second input

print("::: User Menu :::")
options = ["Option 3", "Option 4", "Option 5"]
for option in options:
    # prints out option 
    print("- " + option)
resultTwo = input("selection: ")



# Instead of separate copies of code getting a user input:
# turn into a function:
def GetMenuSelection(menuOptions, inputPrompt):
    print("::: User Menu :::")
    for option in menuOptions:
        # prints out option 
        print("- " + option)
        
    # get input
    return input(inputPrompt)
```