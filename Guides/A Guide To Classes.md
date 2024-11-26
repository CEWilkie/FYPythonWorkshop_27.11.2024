# Classes

#### [Return to Contents](../README.md)

Additional Materials found at:
<br> [Python Classes - w3schools](https://www.w3schools.com/python/python_classes.asp)
<br> [Python OOP Concepts - GeeksForGeeks](https://www.geeksforgeeks.org/python-oops-concepts/?ref=outind)
<br> [Python Polymorphism](https://www.w3schools.com/python/python_polymorphism.asp)

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

From the class above, you can observe the class data members `name` and `numbers`. These
members exist for each object instance of the class, and can be different. Hence, when each
object calls `SayHi()` they output different names and numbers.

Lets go into further detail on the critical elements to class creation:

#### What is `def __init__(self)`?

The `__init__(self, name)` function is a required element of any class definition. It is 
the function utilised for setting up an object from a class. It may be defined with any 
amount of parameters, the only required one being self. The function can then be used to 
assign values to the object data (in this case `name` and `numbers`) on object creation.

Typically, this would be referred to as a constructor, as it "constructs" the object of 
the class. This name is much more universal across languages than `__init__()`, and it 
would be good to make note of it.

some classes may not take any parameters for object creation, and hence only the following
is required:

```python
class MyClass:
    data = []

    def __init__(self):
        # create object!
        pass
```

However, self is a critical element to the `__init__` function, and cannot be omitted. 
Note the usage of pass to indicate that no work needs to be done in the function. Check
out [this page](https://www.w3schools.com/python/ref_keyword_pass.asp) for more info!

#### What is `self`?

self is used to refer to the current object of the class that is utilising the data or
calling the function. 

```python
class MyClass:
    # avoids having to define name as an empty string unecessarily
    # and lets you know what you expect name to be. See Types Guide for more info
    name : str

    def __init__(self, name):
        self.name = name

    def SayHi(self):
        print("My name is " + self.name)
    
# so when we create a class instance, MyClass() calls __init__()
object = MyClass("Greg")

# and when __init__(self, name) is called, it becomes:

# __init__(object, "Greg"):
#   object.name = "Greg"
```

self is required for any function in a class which utilises class data, as a reference to
a class is required in order to fetch the data from it. But this does mean that a class
function which does not use or manipulate the class's data does not need to call Self

```python
class MyClass:
    name : str

    def __init__(self, name):
        self.name = name

    @staticmethod
    def SayHi():
        print("My name is set to something")
```

This code utilises the tag @staticmethod so that the class recognises that self is not
required. This makes the function a static function. This also has the additional 
benefit of not requiring any object instance to call the function, meaning that the 
following two calls of `SayHi()` are equally valid.

```python
object = MyClass("name")
object.SayHi()

# same as
MyClass.SayHi()
```

##
### Class Inheritance and Polymorphism

- Child Class : a class which inherits properties from another class
- Parent Class : a class which provides properties for another class
- Polymorphism : where functions with the same name do different things

Class inheritance is where you define a class to take on all properties of a given "parent" class structure, in the 
aims of having a system of generic and specialised data structures for your program. Parent classes provide data members
and functions which are accessible to the child class, and the child class can then define its own specialised data and
functions *not* acccessible to the parent class.

Classes can inherit from as many classes as needed, and likewise Classes can be inherited by as many classes as needed.
However, I would suggest that you aim to typically only have classes inherit from 1 class - this will help reduce any
potential complexities in class-relationships and keeps things clear and obvious. Classes can also inherit from a class
which inherits from another class, but again I would advise that you keep your inheritance simple to start with.

Parent classes which are inherited from do not need any special syntax or functions to enable inheritance. However, the
child class will. The following code will be used for a better explanation of some of these features

```python
from random import randint

class Parent:
    name : str
    age : int
    def __init__(self, name):
        self.name = name
        self.age = randint(30,40)

    def SayHi(self):
        print("I am the Parent Class " + self.name)

    def SharedFunction(self):
        print("This function is the same for parents and children!")

        
class Child(Parent):
    def __init__(self, name):
        super().__init__(name)
        self.age = randint(3,10)

    def SayHi(self):
        print("I am the Child Class " + self.name)

    def ChildOnlyFunction(self):
        print("This function is only available to the child class")


parent = Parent("Boris")
child = Child("Timmy")

# outputs commented

parent.SayHi()              # I am the Parent Class Boris
parent.SharedFunction()     # This function is the same for parents and children!

child.SayHi()               # I am the Child Class Timmy
child.SharedFunction()      # This function is the same for parents and children!
child.ChildOnlyFunction()   # This function is only available to the child class
```

#### Inheritance Syntax

In the code above, note the declaration of the Child class `Child(Parent)` taking in Parent as a parameter. In order to
set up an inheritance relationship, all parent classes that Child inherits from must be present within the backets. 
Note that brackets after the class name is *only* necessary when classes are inheriting from another class:

```python
# does not inherit
class SingleClass:
    pass

# Parent Class, but does not itself inherit from anything
class Parent:
    def __init__(self):
        pass

# Inheritance from Parent class
class Child(Parent):
    def __init__(self):
        super().__init__()
```

The other key detail for a child class is the usage of `super().__init__()` within the child class's `__init__()` 
function. This code will call call the `__init__()` function of the parent class whenever an object of the child class
is constructed. Parameters can be passed through to the `super().__init__()` call through giving the child class's
`__init__()` function parameters:

```python
class Parent:
    name : str
    def __init__(self, name):
        self.name = name
        
class Child(Parent):
    def __init__(self, name):
        # utilise the parent constructor to set the name of child
        super().__init__(name) 
```

`super()` refers to the parent class of `Child` - `Parent` and is equivalent to calling 
`Parent.__init__(self, name)`. I would actually recommend this over utilising `super()`, as it again helps with making
inheritance clear, and additionally makes multiple inheritance much easier than utilising `super()` (Not to suggest
that it is the 100% correct or perfect way, as either is acceptable).

With regards to multiple inheritance, there is not much different from single-class inheritance other than making sure
all parent classes are initialised, and that no functions or variables share the same name. If a variable or function
name is shared, then the order in which inherited classes are initialised will matter. 

In the following code, class C inherits from A and B, and A and B both take in a different parameter value. So I have
utilised separate `__init__(self, param)` calls for A and B.

```python
class A:
    val : int
    def __init__(self, a):
        self.val = a


class B:
    value : int
    def __init__(self, b):
        self.value = b


class C(A, B):
    def __init__(self, a, b):
        A.__init__(self, a)
        B.__init__(self, b)

    def Results(self):
        print(self.val + self.value)


c = C(3, 4)
c.Results() # outputs 7
```

#### Polymorphism

As mentioned, classes inherit both data and functions. Functions that are inherited by a child class can have their
definitions changed, yet still be called from the same function name. This is particularly useful for class 
specialisation, where all classes will want at minimum some form of generic default function, however some particular 
classes can choose to alter the function to their needs.

```python
class Parent:
    name: str
    
    def __init__(self, name):
        self.name = name

    def SayHi(self):
        print("I am the Parent Class " + self.name)


class Child(Parent):
    age : int
    
    def __init__(self, name, age):
        Parent.__init__(self, name)
        self.age = age
        
    def SayHi(self):
        print("I am the Child Class " + self.name + 
              ", and I am " + str(self.age) + " years old!")


parent = Parent("Boris")
child = Child("Timmy", 7)
parent.SayHi()
child.SayHi()
```

A rather basic example, but here Child changes the instructions of SayHi() to make use of its age data. This data
is not part of the Parent class, and so this is an example of specialisation within the Child class.