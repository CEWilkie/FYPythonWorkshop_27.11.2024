# Loops

#### [Return to Contents](../README.md)

Additional Materials found at:<br>
[Loops In Python - GeeksForGeeks](https://www.geeksforgeeks.org/loops-in-python/?ref=outind)

### What are they?

Loops perform an execution of some set instructions multiple times, depending on the 
conditions applied. These conditions are evaluated to some true or false result, with 
true results permitting the loop to continue going.

Loops will perform the full set of executions within them before returning to checking
and/or updating their conditions. The only exceptions are when `break` is explicitly called
to exit from a loop early, or an error occurs halting the program entirely.

##
### Types of Loops

#### For Loop

The For Loop is used to iterate over a sequence. This may be a sequence of numbers
or items. For each iteration, a sequence of instructions are carried out.

Below are examples of implementations of for loops, with good times to implement them
and how they differ. 

- #### For (Range-based) Loop

The range() function can take a starting value, a final value, and a step value.
It will return a list of values, starting at the start value, provided the values are
less than the final value.

(I suppose this also means that range-based for loops are also secretly just item-based
loops, but shhhh dont worry about that)

```python
print(list(range(5)))
# outputs: [0, 1, 2, 3, 4]

print(list(range(2, 5)))
# outputs: [2, 3, 4]

print(list(range(3, 27, 5)))
# outputs: [3, 8, 13, 18, 23]
```

Ranges are useful to ensure that a loop happens only a set number of times. For example, 
this function which returns the required power of a number:

```python
def RaiseToIntPower(num, power):
    result = num
    for p in range(1, power):
        result *= num

    return result
```

Alternatively, the values returned by a range function can be used as indicies for a list. 
Here, in combination with the len() function to retrieve the number of elements in a list, 
the loop iterates over each pair of string and int to print out a message:

```python
myList = ["Apples", 15, "Bananas", 8, "Carrots", 4343243]

for i in range(0, len(myList), 2):
    print("I have " + str(myList[i+1]) + " " + myList[i] + "!")
```

- #### For (item-based) Loop

Item-based for loops can be used to iterate over each item in a list. This can be very useful
for a list of objects where a function is to be called for each of them - such as updating a
position of an enemy in a pygame application.

```python
class MyClass:
    def __init__(self):
        print("class made")

    def SayHi(self):
        print("Hi from " + str(self))

classList = [MyClass(), MyClass(), MyClass()]

for c in classList:
    c.SayHi()
```

however, using this loop method alone won't actually let you change the contents or value of
item. Attempting to redefine c as - for example - "Hi!" during the loop will mean that the list
remains unchanged, and c is redefined locally to be a string of "Hi!"

```python
myList = ["Original"]

for msg in myList:
    msg = "New"
    print(msg) 
    # prints "New"

for msg in myList:
    print(msg) 
    # prints "Original", meaning list 
    # is actually unchanged from previous loop
```

- #### For (Enumeration-Item-Based) Loop

This style of for loop can bridge the gap between item and index based loops through the use of
the `enumerate()` function. Enumerate takes in a list of items, and an optional start value 
(default is 0). It returns a list where each item of the original list has been paired up with a
numeric value in the format `[(index, item), (index2, item2), (index3, item3), ...]`

```python
myList = ["Apple", "Cat", "Boris Johnson", "Boeing 787-9", "Crippling Debt"]

# unpacks index and item from the enumerated list
for index, item in enumerate(myList, 1):
    print("I have " + str(index) + " " + str(item) + "!")
```

It also now allows us to bypass the issue with item-based for loops, where the item in a list
could not be changed during the loop. Via the following loop, through implementing an enumerate
function to obtain an index of each item, we can access the list at said index to change it

```python
myList = ["Value One", "Value Two", "Value Three"]

for index, item in enumerate(myList):
    print(item)
    myList[index] = "New Value"
    
for item in myList:
    print(item)
```


#### While Loop

While loops continuously run whilst a condition is true. The condition is re-evaluated each time
the instructions within the loop is ran through until becoming false. Hence it can be easy to 
make infinite loops whilst using whiles, which require a `break` command to exit.

Whilst these cases are often undesirable, they are really useful for games. Within a game, you
will likely implement a "Gameloop" which is an infinite loop using a while constantly running
code to allow game updates to occur.

The condition of a while loop is able to be anything which can evaluate into some boolean 
expression. Below are some examples:

```python 
# Infinite while - requires break
while True:
    break

# A potential improvement to using break and while True
running = True
while running:
    running = False

# Evalutating a condition, in this case comparing the user input string to "bye"
usrInput = ""
while usrInput != "bye":
    usrInput = input("Enter Input: ")

# Assignment while, where line is assigned and compared to an empty string at 
# the start of each loop (there are way easier methods for printing file 
# contents than this by the way!)
file = open("../ImportFiles/BasicTextFile1.txt")
while (line := file.readline()) != "":
    print(line, end="")
```

##
### Break, Continue and Else

`Break` and `Continue` are two keywords often particularly helpful to employ in your loops. Break
will cause an immediate exit from the loop, regardless of the current state of the loop condition.
Continue will result in the current iteration halting, and the loop immediately proceeding to the 
next iteration.

```python
def FindChar(string, char):
    index = 0
    for c in string:
        if c == char:
            break
        
        index += 1

    return index
```

`break` is useful for ensuring that loops do not continue forever, and providing early exits for
when a loop is no longer required to run. The above example is a function that finds the index of
a specific character in a string. should the character appear, the program no longer needs to 
iterate over the string, hence it breaks the loop early.

```python
myStock = {"apples" : 15, "bananas" : 7, "strawberries" : 12}

def PrintLowStock(stock):
    for item in stock:
        if stock[item] > 10:
            continue

        # item has low stock!
        print(item + " has low stock! Only: " + str(stock[item]) + " remaining!")

PrintLowStock(myStock)
```

`continue` is useful for ensuring that actions only occur if particular conditions are met. In this
loop, we only want to inform the user of low stock when the condition (the stock count is <= 10)
is met. Hence whenever the stock count is greater than 10 we continue to the next iteration of the 
loop.

```python
nums = [1, 9, 7, 3, 11]

for n in nums:
    if n % 2 == 0:
        print("list contains even number")
        break
        
# only when no even numbers
else:
    print("list does not contain an even number")
```

`else` blocks when attached to a loop always execute after a loop completes. The only exception
being when a loop is exited via a `break` command - where the else code will not execute.