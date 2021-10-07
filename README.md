# [What’s New In Python 3.10](https://docs.python.org/3.10/whatsnew/3.10.html)
- [Index of Python Enhancement Proposals (PEPs)](https://www.python.org/dev/peps/)
- [PEP8: Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [PEP20: The Zen of Python](https://www.python.org/dev/peps/pep-0020/)

![python310](Docs/python310.jpg)

## Getting Started
- New syntax features:
    - [Structural Pattern Matching](#Structural-Pattern-Matching)
    - [Parenthesized context managers](#Parenthesized-context-managers) 

- New features in the standard library:
    - [Add Optional Length-Checking To zip](#zip)

- [Interpreter improvements error messages](#Better-error-messages)
    1. SyntaxError
    2. IndentationError
    3. AttributeErrors

- [New typing features](#typing)
    - Allow writing union types as X | Y
    - Explicit Type Aliases
    - Parameter Specification Variables

- [Improved Modules](#Improved-Modules)


- [Optimizations](#Optimizations)

- Important deprecations, removals or restrictions:
    - Require OpenSSL 1.1.1 or newer
    - Deprecate distutils module.
    - Deprecate and prepare for the removal of the wstr member in PyUnicodeObject.
    - Remove Py_UNICODE encoder APIs
    - Add optional EncodingWarning



# Structural-Pattern-Matching
```python
match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case _:
        <action_wildcard>
```

```python
def httperror(status):
    match status:
        case 400: 
            return "Bad request"
        case 401 | 403:
            return "Not allowed"
        case 404:
            return "Not found"
        case _:
            return "Somthing's wrong with the internet"

print(httperror(406))
```

```python
# point is an (x, y) tuple
x = 9
y = 10
point = (x, y)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
```

```python
from enum import Enum
class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2

color = Color.RED

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
    case _:
        print("Not Color")
```



# Parenthesized-context-managers
- what is context manager?
for example : with in open files
```python
with open('myfilename.txt') as f:
    pass
```

- create multiple context manager in python310

```python
class Log_Manager:
    def __enter__(self):
        print('Entering context manager')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exiting context manager')
```

```python
class Test_Context_Manager:
    def __enter__(self):
        print('task1')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('task2')
```

our function:
```python
def do_task():
    print("do task")
```

- python3.9
```python
with Log_Manager():
    do_task()
```

- Parenthesized context managers

```python
with (
    Log_Manager() as ctx1,
    Test_Context_Manager() as ctx2,
):
    do_task()
```



# zip
- what is zip : The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.

- strict in python3.10
```python
name = ("Mohammad", "Ali", "Reza")
family = ("Taghizadeh", "Mohammadi", "Rahimi",  "Felani", "Behamani")
fullname_tuple = zip(name, family, strict=True) # strict(yek dandeh) => ValueError: zip() argument 2 is longer than argument 1
print(list(fullname_tuple))
```

- we can use zip() for list objects
```python
name = ["Mohammad", "Ali", "Reza"]
family = ["Taghizadeh", "Mohammadi", "Rahimi",  "Felani"]
fullname_tuple = zip(name, family)
print(list(fullname_tuple))
```



# Better-error-messages

## SyntaxError

```python
mydict = {9: 1, 18: 2, 19: 2, 27: 3, 28: 3, 29: 3, 36: 4, 37: 4,
some_other_code = foo()
output: SyntaxError: '{' was never closed 
```

```python
print("hello world!" 
print("hello world!")
output: SyntaxError: '(' was never closed
```

```python
try:
    x = 2
something = 3
```

```python
number = "mohammad"
if name = "mohammad": 
    pass    
```

## IndentationError
```python
def task():
    if True:
    x = 2
```

## AttributeErrors : errors suggestions
```python
product = "car"
print(produc) 

output: NameError: name 'produc' is not defined. Did you mean: 'product'?
```



# typing

- Union Operator => python3.9 => |, |= 

```python
dict1 = {
    1: 'a',
    2: 'b', 
    3: 'c', 
    4: 'in both',
}
dict2 = {
    4: 'but different', 
    5: 'd', 
    6: 'e'
}

print(dict1 | dict2) 
dict1 |= dict2
print(dict1)
```

- New Type Union Operator

```python
def square(number: int | float):
    print(type(number))
    return number ** 2

# Instead of 
from typing import Union
def old_square(number: Union[int, float]):
    return number ** 2

print(square(2.2))
print(square(2))
```



# Improved Modules
```python
asyncio, argparse
base64,
contextlib,
dataclasses,
hashlib,
os,
pathlib, pprint,
statistics, socket, ssl, sqlite3,
threading, traceback, typing,
unittest,
xml
```



# Optimizations
- Constructors str(), bytes() and bytearray() are now faster (around 30–40% for small objects).

- The runpy module now imports fewer modules. The python3 -m module-name command startup time is 1.4x faster in average. On Linux, python3 -I -m module-name imports 69 modules on Python 3.9, whereas it only imports 51 modules (-18) on Python 3.10.