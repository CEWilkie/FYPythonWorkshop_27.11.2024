from random import randint


class MyClass:
    # Class Data
    name = ""
    numbers = []

    def __init__(self, name):
        self.name = name

        # give class some numbers
        self.numbers = [randint(0,50) for _ in range(5)]

    def SayHi(self):
        print("My name is: " + self.name +
              "! My numbers are: " + str(self.numbers))


objectList = [MyClass("Bob"), MyClass("Jackson"), MyClass("Boris"), MyClass("Gary")]
for object in objectList:
    object.SayHi()