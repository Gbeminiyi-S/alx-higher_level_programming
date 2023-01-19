# 0x08. Python - More Classes and Objects
An introductory project on:

- What is OOP
- What are and how to use public, protected and private attributes
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is the __dict__ of a class and/or instance of a class and what does it contain
- How to use the getattr function
- What is the Pythonic way to write getters and setters in Python
- What are the special __str__ and __repr__ methods and how to use them
- What is a class method
- What is a static method
- What is the difference between a object attribute and a class attribute

## Requirements
- Files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Codes are checked with the pycodestyle (version 2.8.*)
- The first line of all files are exactly #!/usr/bin/python3
- All files are executable

## File Descriptions
### Mandatory
[0-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x08-python-more_classes/0-rectangle.py) -  an empty class `Rectangle` that defines a rectangle

[1-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x08-python-more_classes/1-rectangle.py) -  a class `Rectangle` that defines a rectangle by: (based on [0-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x08-python-more_classes/0-rectangle.py))
- Private instance attribute: `width`:
    - property `def width(self):` to retrieve it
    - property setter `def width(self, value):` to set it:
          - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
          - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height:`
    - property `def height(self):` to retrieve it
    - property setter `def height(self, value):` to set it:
          - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
          - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`

[2-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x08-python-more_classes/2-rectangle.py) -  a class `Rectangle` that defines a rectangle by: (based on [1-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x08-python-more_classes/1-rectangle.py))
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
     - if `width` or `height` is equal to `0`, perimeter is equal to `0`
     
[3-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x08-python-more_classes/3-rectangle.py) -  a class `Rectangle` that defines a rectangle by: (based on [2-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x08-python-more_classes/2-rectangle.py))
- `print()` and `str()` should print the rectangle with the character `#`:
      - if `width` or `height` is equal to `0`, return an empty string
      
[4-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x08-python-more_classes/4-rectangle.py) -  a class `Rectangle` that defines a rectangle by: (based on [3-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x08-python-more_classes/3-rectangle.py))
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`

[5-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x08-python-more_classes/5-rectangle.py) -  a class `Rectangle` that defines a rectangle by: (based on [4-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x08-python-more_classes/4-rectangle.py))
- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted

[6-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x08-python-more_classes/6-rectangle.py) -  a class `Rectangle` that defines a rectangle by: (based on [5-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x08-python-more_classes/5-rectangle.py))
- Public class attribute `number_of_instances:`
    - Initialized to `0`
    - Incremented during each new instance instantiation
    - Decremented during each instance deletion
    
 [7-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x08-python-more_classes/7-rectangle.py) -  a class `Rectangle` that defines a rectangle by: (based on [6-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x08-python-more_classes/6-rectangle.py))
- Public class attribute `print_symbol`:
    - Initialized to `#`
    - Used as symbol for string representation
    - Can be any type
    
[8-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x08-python-more_classes/8-rectangle.py) -  a class `Rectangle` that defines a rectangle by: (based on [7-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x08-python-more_classes/7-rectangle.py))
- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
    - `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
    - `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2` must be an instance of `Rectangle`
    - Returns `rect_1` if both have the same area value

[9-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x08-python-more_classes/9-rectangle.py) -  a class `Rectangle` that defines a rectangle by: (based on [8-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x08-python-more_classes/8-rectangle.py))
Class method def square(cls, size=0): that returns a new Rectangle instance with width == height == size
