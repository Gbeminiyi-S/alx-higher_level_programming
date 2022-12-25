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
