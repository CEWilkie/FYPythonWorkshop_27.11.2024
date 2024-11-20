# Functions

Functions are a set of instructions executed whenever the function name is called. 
These instructions may include acting or utilising some given parameters in the function,
such as a String of text, or int number. Additionally, they may provide a return value
that can then be further used.

```python
# valid code:

# define function
def Add(_a, _b):
    return _a + _b
    
# call function
result = Add(5, 6)
```

Functions should be declared before any usages within code, otherwise python wont know
what the function being called is supposed to do. Typically this will be highlighted 
with a helpful error message to let you know.

```python
# invalid code:

# call function
result = Add(5, 6)

# define function
def Add(_a, _b):
    return _a + _b 
```