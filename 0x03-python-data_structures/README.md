# 0x03. Python - Data Structures: Lists, Tuples
An introductory project on:

- What are lists and how to use them
- What are the differences and similarities between strings and lists
- What are the most common methods of lists and how to use them
- How to use lists as stacks and queues
- What are list comprehensions and how to use them
- What are tuples and how to use them
- When to use tuples versus lists
- What is a sequence
- What is tuple packing
- What is sequence unpacking
- What is the `del` statement and how to use it

## Requirements
### Python Scripts
- Files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Codes are checked with the pycodestyle (version 2.8.*)

### C
- Files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- No more than 5 functions per file
- Our main.c files might be different from the one shown in the examples
- The prototypes of all functions are included in the header file called [lists.h](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x03-python-data_structures/lists.h)

## File Descriptions
### Mandatory
[0-print_list_integer.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x03-python-data_structures/0-print_list_integer.py) - a function that prints all integers of a list
   - Prototype: `def print_list_integer(my_list=[]):`
   - not allowed to cast integers into strings
   - use `str.format()` to print integers

[1-element_at.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x03-python-data_structures/1-element_at.py) - a function that retrieves an element from a list like in C
  - Prototype: `def element_at(my_list, idx):`
  - If `idx` is negative, the function should return `None`
  - If `idx` is out of range (> of number of element in `my_list`), the function should return `None`
  - not allowed to import any module
  - not allowed to use `try/except`

[2-replace_in_list.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x03-python-data_structures/2-replace_in_list.py) - a function that replaces an element of a list at a specific position (like in C)
  - Prototype: `def replace_in_list(my_list, idx, element):`
  - If `idx` is negative, the function should not modify anything, and returns the original list
  - If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list
  - not allowed to import any module
  - not allowed to use `try/except`

[3-print_reversed_list_integer.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x03-python-data_structures/3-print_reversed_list_integer.py) - a function that prints all integers of a list, in reverse order.
  - Prototype: `def print_reversed_list_integer(my_list=[]):`
  - not allowed to cast integers into strings
  - use `str.format()` to print integers

[4-new_in_list.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x03-python-data_structures/4-new_in_list.py) -  a function that replaces an element in a list at a specific position without modifying the original list (like in C)
  - Prototype: def new_in_list(my_list, idx, element):`
  - If `idx` is negative, the function should not modify anything, and returns the original list
  - If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list

[5-no_c.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x03-python-data_structures/5-no_c.py) - a function that removes all characters `c` and `C` from a string.
  - Prototype: `def no_c(my_string):`
  - The function should return the new string
  - not allowed to use `str.replace()`
