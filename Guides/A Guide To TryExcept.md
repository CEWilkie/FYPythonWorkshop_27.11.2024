# TryExcept

#### [Return to Contents](../README.md)

Additional Materials found at:
<br>[Python Try Except - w3schools](https://www.w3schools.com/python/python_try_except.asp)

### What is TryExcept?

In python, exception or error handling is done via the use of `try ... except` blocks. Typically, you
may have observed python stop running due to encountering an error. However, through the use of
exception handling we can prevent a total shutdown of the program by adding in extra security and 
management in areas where we know functions may occur.

```python
try:
    # do something that could cause an issue
except:
    # uh oh, an error occured! This code will now execute...
```

##
### What are the components of TryExcept?

TryExcept is composed of up to 4 blocks of code which can execute. Those blocks are the `try`, 
`except`, `else` and `finally` blocks. Below, each block's purpose will be covered in more detail.

#### Try and Except

The `try` block will allow you to execute code which may have errors in it safely. It signifies that
there is a potential for an error to occur and that it is being sufficiently handled by the program.

`except` is the code which executes when the try block code triggers an error. Except is capable of
catching specific errors from the try block, and executing code dependant upon that type of error.
Both `try` and `except` (or alternatively `finally`) are required components for making proper 
try ... except routine. 

```python
list = [2, 15]

for item in list:
    try:
        if item == 2:
            print(x)

        else:
            print("the value of x is " + item)

    except NameError:
        print("x was undefined!")

    except TypeError:
        print("x is not a string!")

    except:
        print("somehow a different error occurred!")
```

The loop above shows an example of catching two different errors. This is done by defining the 
error type being caught by the `except` block. Alternatively, a plain `except` can be used to catch
any and all errors that may be thrown by the try block.

#### Finally and Else

The `finally` block will allow for you to execute code regardless of the results of what occurs in 
the try and except blocks. This can be useful for cleaning up resources such as opened files, or 
just ensuring that code will execute, even if an early return occurs during a try or except block.

```python
def Foo():
    try:
        print(x)
    except:
        print("no x defined")
        return
    finally:
        print("this was executed after returning")

Foo()
```

`else` blocks can be used to run code when specifically no issues arose. You may want to implement
this if you have two operations that could raise an error, but you explicitly do not want to catch
the second operations potential error. Or alternatively use it for logging purposes.

```python
try:
    x = 15
    print(x)
except NameError:
    print("x was undefined")
else:
    print("operation succeeded")
```


#### Throw

Whilst not an actual component of `try ... except`, the throw keyword is still worth mentioning.
This keyword allows for you to throw specific exceptions should an error occur. This can be useful
when making functions which require specific types of values. For example, this function which 
requires a list of numbers (integer or decimal) only

```python
def SumIntegers(nums):
    result = 0
    for num in nums:
        if type(num) not in [int, float]:
            raise TypeError("Only numbers are allowed!")
        else:
            result += num

    return result
```

##
### Some Helpful Exceptions

| Function                  | Exception  |                        When                         |
|:--------------------------|:----------:|:---------------------------------------------------:|
| int() or other type casts | ValueError |         When the value cannot be converted          |
| open()                    |  OSError   |            When the file failed to open             |
| - + / *   maths functions | TypeError  | When attempting to use with a number and non-number |

Typically, if you search for a function's documentation then it will be able to inform you
about the errors that it raises.