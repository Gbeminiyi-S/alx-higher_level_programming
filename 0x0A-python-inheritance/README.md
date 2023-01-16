# 0x0A. Python - Inheritance
An introductory project on:

- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions
## Requirements
### Python Scripts
- Files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Codes are checked with the pycodestyle (version 2.8.*)
### Python Test Cases
- All test files should be inside a folder tests
- All test files should be text files (extension: `.txt`)
- All tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`) and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

## File Descriptions
### Mandatory
[0-lookup.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/0-lookup.py) - a function that returns the list of available attributes and methods of an object
- Prototype: `def lookup(obj):`
- Returns a `list` object

[1-my_list.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/1-my_list.py) - a class `MyList` that inherits from `list`
- Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
- You can assume that all the elements of the list will be of type `int`
- [1-my_list.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/tests/1-my_list.txt): Test Case

[2-is_same_class.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/2-is_same_class.py) - a function that returns `True` if the object is exactly an instance of the specified class ; otherwise `False`
- Prototype: `def is_same_class(obj, a_class):`

[3-is_kind_of_class.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/3-is_kind_of_class.py) - a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise `False`
- Prototype: `def is_kind_of_class(obj, a_class):`

[4-inherits_from.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/4-inherits_from.py) - a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise `False`
- Prototype: `def inherits_from(obj, a_class):`

[5-base_geometry.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/5-base_geometry.py) - an empty class `BaseGeometry`

[6-base_geometry.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/6-base_geometry.py) - a class `BaseGeometry` (based on [5-base_geometry.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/5-base_geometry.py))
- Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`

[7-base_geometry.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/7-base_geometry.py) - a class `BaseGeometry` (based on [6-base_geometry.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/6-base_geometry.py))
- Public instance method: `def integer_validator(self, name, value):` that validates `value:`
    - you can assume `name` is always a string
    - if `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`
    - if `value` is less or equal to `0`: raise a `ValueError` exception with the message `<name> must be greater than 0`
 - [7-base_geometry.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/tests/7-base_geometry.txt): Test Case
 
[8-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/8-rectangle.py) - a class `Rectangle` that inherits from `BaseGeometry` (based on [7-base_geometry.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/7-base_geometry.py))
 - Instantiation with `width` and `height`: `def __init__(self, width, height):`
      - `width` and `height` must be private. No getter or setter
      - `width` and `height` must be positive integers, validated by `integer_validator`
      
[9-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/9-rectangle.py) - a class `Rectangle` that inherits from `BaseGeometry` [7-base_geometry.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/7-base_geometry.py) (task based on [8-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/8-rectangle.py))
- the `area()` method must be implemented
- `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`

[10-square.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/10-square.py) a class Square that inherits from Rectangle [9-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/9-rectangle.py)
- Instantiation with `size`: `def __init__(self, size):`
    - `size` must be private. No getter or setter
     - `size` must be a positive integer, validated by `integer_validator`
- the `area()` method must be implemented

[11-square.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/11-square.py) - a class `Square` that inherits from `Rectangle` [9-rectangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/9-rectangle.py) (task based on [10-square.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/10-square.py))
- `print()` should print, and `str()` should return, the square description: `[Square] <width>/<height`
### Advanced
[100-my_int.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/100-my_int.py) - a class `MyInt` that inherits from `int`
- `MyInt` is a rebel. `MyInt` has `==` and `!=` operators inverted

[101-add_attribute.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0A-python-inheritance/101-add_attribute.py) - a function that adds a new attribute to an object if it’s possible
- Raise a `TypeError` exception, with the message `can't add new attribute` if the object can’t have new attribute
- You are not allowed to use `try/except`
