# 0x06. Python - Classes and Objects
An introductory project on:

- What is OOP
- What are and how to use public, protected and private attributes
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is the __dict__ of a class and/or instance of a class and what does it contain
- How to use the getattr function

## Requirements
- Files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Codes are checked with the pycodestyle (version 2.8.*)
- The first line of all files are exactly #!/usr/bin/python3
- All files are executable


## File Descriptions
### Mandatory
[0-square.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x06-python-classes/0-square.py) - an empty class `Square` that defines a square

[1-square.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x06-python-classes/1-square.py) - a class `Square` that defines a square by:
- Private instance attribute: `size`
- Instantiation with `size` (no type/value verification)

[2-square.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x06-python-classes/2-square.py) - a class `Square` that defines a square by:
- Private instance attribute: `size`
- Instantiation with optional `size`: `def __init__(self, size=0):`
    - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`

[3-square.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x06-python-classes/3-square.py) - a class `Square` that defines a square by:
- Private instance attribute: `size`
- Instantiation with optional `size`: `def __init__(self, size=0):`
    - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Public instance method: `def area(self):` that returns the current square area

[4-square.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x06-python-classes/4-square.py) - a class `Square` that defines a square by:
- Private instance attribute: `size`:
    - property `def size(self):` to retrieve it
    - property setter `def size(self, value):` to set it:
    - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Instantiation with optional `size`: `def __init__(self, size=0):`
    - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Public instance method: `def area(self):` that returns the current square area

[5-square.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x06-python-classes/5-square.py) - a class `Square` that defines a square by:
- Private instance attribute: `size`:
    - property `def size(self):` to retrieve it
    - property setter `def size(self, value):` to set it:
    - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Instantiation with optional `size`: `def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
    - if `size` is equal to 0, print an empty line

[6-square.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x06-python-classes/6-square.py) - a class `Square` that defines a square by:
- Private instance attribute: `size`:
    - property `def size(self):` to retrieve it
    - property setter `def size(self, value):` to set it:
    - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Private instance attribute: `position:`
    - property `def position(self):` to retrieve it
    - property setter `def position(self, value):` to set it:
          - `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`
- Instantiation with optional `size` and optional position: `def __init__(self, size=0, position=(0, 0)):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
    - if `size` is equal to 0, print an empty line
    - `position` should be use by using space - *Don’t fill lines by spaces* when `position[1] > 0`
    
[101-square.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x06-python-classes/101-square.py) - a class `Square` that defines a square by: (based on [6-square.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x06-python-classes/6-square.py))
- Printing a `Square` instance should have the same behavior as `my_print()`

[102-square.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x06-python-classes/102-square.py) - a class `Square` that defines a square by:
- Private instance attribute: `size`:
    - property `def size(self):` to retrieve it
    - property setter `def size(self, value):` to set it:
    - `size` must be a number (float or integer), otherwise raise a `TypeError` exception with the message `size must be a number`
    - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Instantiation with optional `size`: `def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- `Square` instance can answer to comparators: `==`, `!=`, `>`, `>=`, `<` and `<=` based on the square area

[103-magic_class.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x06-python-classes/103-magic_class.py) - a Python class MagicClass that does exactly the same as the following Python bytecode:

```
Disassembly of __init__:
 10           0 LOAD_CONST               1 (0)
              3 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (_MagicClass__radius)

 11           9 LOAD_GLOBAL              1 (type)
             12 LOAD_FAST                1 (radius)
             15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             18 LOAD_GLOBAL              2 (int)
             21 COMPARE_OP               9 (is not)
             24 POP_JUMP_IF_FALSE       60
             27 LOAD_GLOBAL              1 (type)
             30 LOAD_FAST                1 (radius)
             33 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             36 LOAD_GLOBAL              3 (float)
             39 COMPARE_OP               9 (is not)
             42 POP_JUMP_IF_FALSE       60

 12          45 LOAD_GLOBAL              4 (TypeError)
             48 LOAD_CONST               2 ('radius must be a number')
             51 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             54 RAISE_VARARGS            1
             57 JUMP_FORWARD             0 (to 60)

 13     >>   60 LOAD_FAST                1 (radius)
             63 LOAD_FAST                0 (self)
             66 STORE_ATTR               0 (_MagicClass__radius)
             69 LOAD_CONST               3 (None)
             72 RETURN_VALUE

Disassembly of area:
 17           0 LOAD_FAST                0 (self)
              3 LOAD_ATTR                0 (_MagicClass__radius)
              6 LOAD_CONST               1 (2)
              9 BINARY_POWER
             10 LOAD_GLOBAL              1 (math)
             13 LOAD_ATTR                2 (pi)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE

Disassembly of circumference:
 21           0 LOAD_CONST               1 (2)
              3 LOAD_GLOBAL              0 (math)
              6 LOAD_ATTR                1 (pi)
              9 BINARY_MULTIPLY
             10 LOAD_FAST                0 (self)
             13 LOAD_ATTR                2 (_MagicClass__radius)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE
```
