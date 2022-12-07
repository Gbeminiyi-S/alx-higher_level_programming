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

[6-print_matrix_integer.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x03-python-data_structures/6-print_matrix_integer.py) - a function that prints a matrix of integers

[7-add_tuple.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x03-python-data_structures/7-add_tuple.py) - a function that adds 2 tuples
- Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
- Returns a tuple with 2 integers:
   - The first element should be the addition of the first element of each argument
   - The second element should be the addition of the second element of each argument
- If a tuple is smaller than 2, use the value 0 for each missing integer
- If a tuple is bigger than 2, use only the first 2 integers

[8-multiple_returns.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x03-python-data_structures/8-multiple_returns.py) - a function that returns a tuple with the length of a string and its first character
- Prototype: def multiple_returns(sentence):`
- If the sentence is empty, the first character should be equal to `None`

[9-max_integer.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x03-python-data_structures/9-max_integer.py) - a function that finds the biggest integer of a list
- Prototype: `def max_integer(my_list=[]):`
- If the list is empty, return `None`
- You are not allowed to use the builtin `max()`

[10-divisible_by_2.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x03-python-data_structures/10-divisible_by_2.py) - a function that finds all multiples of 2 in a list
- Prototype: `def divisible_by_2(my_list=[]):`
- Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2
- The new list should have the same size as the original list

[11-delete_at.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x03-python-data_structures/11-delete_at.py) - a function that deletes the item at a specific position in a list
- Prototype: `def delete_at(my_list=[], idx=0):`
- If `idx` is negative or out of range, nothing change (returns the same list)
- You are not allowed to use `pop()`

[12-switch.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x03-python-data_structures/12-switch.py) - Complete the [source code](https://github.com/holbertonschool/0x03.py/blob/master/12-switch_py) in order to switch value of `a` and `b`
