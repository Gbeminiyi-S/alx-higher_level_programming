# 0x04. Python - More Data Structures: Set, Dictionary
An introductory project on:

- What are sets and how to use them
- What are the most common methods of set and how to use them
- When to use sets versus lists
- How to iterate into a set
- What are dictionaries and how to use them
- When to use dictionaries versus lists or sets
- What is a key in a dictionary
- How to iterate over a dictionary
- What is a lambda function
- What are the map, reduce and filter functions
## Requirements
### General
- Files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- The first line of all files should be exactly `#!/usr/bin/python3`
- All files must be executable
- Codes are checked with the `pycodestyle` (version 2.8.*)
## File Descriptions
[0-square_matrix_simple.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/0-square_matrix_simple.py) -  a function that computes the square value of all integers of a matrix
- Prototype: `def square_matrix_simple(matrix=[]):`
- Initial matrix should not be modified
- Returns a new matrix:
  - Same size as `matrix`
  - Each value should be the square of the value of the input

[1-search_replace.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/1-search_replace.py) - a function that replaces all occurrences of an element by another in a new list
- Prototype: `def search_replace(my_list, search, replace):`
- `my_list` is the initial list
- `search` is the element to replace in the list
- `replace` is the new element

[2-uniq_add.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/2-uniq_add.py) - a function that adds all unique integers in a list (only once for each integer)
- Prototype: `def uniq_add(my_list=[]):`

[3-common_elements.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/3-common_elements.py) - a function that returns a set of common elements in two sets
- Prototype: `def common_elements(set_1, set_2):`

[4-only_diff_elements.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/4-only_diff_elements.py) - a function that returns a set of all elements present in only one set
- Prototype: `def only_diff_elements(set_1, set_2):`

[5-number_keys.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/5-number_keys.py) - a function that returns the number of keys in a dictionary
- Prototype: `def number_keys(a_dictionary):`

[6-print_sorted_dictionary.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/6-print_sorted_dictionary.py) - a function that prints a dictionary by ordered keys
- Prototype: `def print_sorted_dictionary(a_dictionary):`
- Keys should be sorted by alphabetic order
- Dictionary values can have any type

[7-update_dictionary.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/7-update_dictionary.py) - a function that replaces or adds key/value in a dictionary
- Prototype: `def update_dictionary(a_dictionary, key, value):`
- `key` argument will be always a string
- `value` argument will be any type
- If a key exists in the dictionary, the value will be replaced
- If a key doesn’t exist in the dictionary, it will be created
 function that deletes a key in a dictionary

[8-simple_delete.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/8-simple_delete.py) -  function that deletes a key in a dictionary
- Prototype: `def simple_delete(a_dictionary, key=""):`
- `key` argument will be always a string
- If a key doesn’t exist, the dictionary won’t change

[9-multiply_by_2.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/9-multiply_by_2.py) - a function that returns a new dictionary with all values multiplied by 2
- Prototype: `def multiply_by_2(a_dictionary):`
- Returns a new dictionary
