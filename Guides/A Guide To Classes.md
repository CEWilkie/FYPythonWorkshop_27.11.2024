# Classes

#### [Return to Contents](../README.md)

Additional Materials found at:
<br> [Python Classes - w3schools](https://www.w3schools.com/python/python_classes.asp)
<br> [Python OOP Concepts - GeeksForGeeks](https://www.geeksforgeeks.org/python-oops-concepts/?ref=outind)

### What are they?

Classes are - at the very base level - structures of data, typically with their own 
inbuilt functions that utilise the stored data. Furthermore, using classes will assist
in streamlining processes where you need to store numerous instances of similar data, and
identifying the relations between sets of data.

Classes however should also be more readily acknowledged as classes and objects. Classes 
the templates from which the data stores (objects) are built from, and outline how those
data stores can be utilised. 

```python
from random import randint


class MyClass:
    # Class Data
    name = ""
    numbers = []

    # Required setup function to initialise the object from the class
    def __init__(self, name):
        self.name = name

        # give class some numbers
        self.numbers = [randint(0,50) for _ in range(5)]

    def SayHi(self):
        print("My name is: " + self.name + 
              "! My numbers are: " + str(self.numbers))

# Now create a new instance of the class, and put those instances into a
# list for easy access
objectList = [MyClass("Bob"), MyClass("Jackson"), MyClass("Boris"), MyClass("Gary")]

# call the class function "SayHi" on each object in the list
for object in objectList:
    object.SayHi()
```