# 0x05. Python - Exceptions
An introductory project on:

- Difference between errors and exceptions
- What are exceptions and how to use them
- When do we need to use exceptions
- How to correctly handle an exception
- What’s the purpose of catching exceptions
- How to raise a builtin exception
- When to implement a clean-up action after an exception

## Requirements
- Files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Codes are checked with the pycodestyle (version 2.8.*)
- The first line of all files are exactly #!/usr/bin/python3
- All files are executable

## File Descriptions
### Mandatory
[0-safe_print_list.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x05-python-exceptions/0-safe_print_list.py) - a function that prints `x` elements of a list
- Prototype: `def safe_print_list(my_list=[], x=0):`
- `my_list` can contain any type (integer, string, etc.)
- Use `try: / except:`
- `len()` not allowed

[1-safe_print_integer.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x05-python-exceptions/1-safe_print_integer.py) - a function that prints an integer with `"{:d}".format()`
- Prototype: `def safe_print_integer(value):`
- `value` can be any type (integer, string, etc.)
- Returns `True` if `value` has been correctly printed (it means the `value` is an integer)
- Otherwise, returns `False`
- Use `try: / except:`
- `type()` not allowed

[2-safe_print_list_integers.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x05-python-exceptions/2-safe_print_list_integers.py) - a function that prints the first `x` elements of a list and only integers
- Prototype: `def safe_print_list_integers(my_list=[], x=0):`
- `my_list` can contain any type (integer, string, etc.)
- `x` can be bigger than the length of `my_list` - if it’s the case, an exception is expected to occur
- Returns the real number of integers printed
- Use `try: / except:`
- `len()` not allowed

[3-safe_print_division.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x05-python-exceptions/3-safe_print_division.py) - a function that divides 2 integers and prints the result
- Prototype: `def safe_print_division(a, b):`
- assume `a` and `b` are integers
- The result of the division should print on the `finally`: section preceded by `Inside result`:
- Returns the value of the division, otherwise: `None`
- Use `try: / except: / finally:`
