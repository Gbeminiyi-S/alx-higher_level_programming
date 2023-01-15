# 0x07. Python - Test-driven development
## Requirements
### Python Scripts
- Files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Codes are checked with the pycodestyle (version 2.8.*)
- All files are executable
### Python Test Cases
- All your test files should be text files (extension: `.txt`)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
## File Descriptions
### Mandatory
[0-add_integer.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x07-python-test_driven_development/0-add_integer.py) - a function that adds 2 integers
  - Prototype: `def add_integer(a, b=98):`
  - `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message `a must be an integer` or `b must be an integer`
  - `a` and `b` must be first casted to integers if they are float
  - Returns an integer: the addition of `a` and `b`
  - **Test_Case:** [0-add_integer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x07-python-test_driven_development/tests/0-add_integer.txt)

[2-matrix_divided.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x07-python-test_driven_development/2-matrix_divided.py) - a function that divides all elements of a matrix
  - Prototype: `def matrix_divided(matrix, div):`
  - `matrix` must be a list of lists of integers or floats, otherwise raise a `TypeError` exception with the message `matrix must be a matrix (list of lists) of integers/floats`
  - Each row of the `matrix` must be of the same size, otherwise raise a `TypeError` exception with the message `Each row of the matrix must have the same size`
  - `div` must be a number (integer or float), otherwise raise a `TypeError` exception with the message `div must be a number`
  - `div` can’t be equal to `0`, otherwise raise a `ZeroDivisionError` exception with the message `division by zero`
  - All elements of the matrix should be divided by `div`, rounded to 2 decimal places
  - Returns a new matrix
  - **Test_Case:** [2-matrix_divided.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x07-python-test_driven_development/tests/2-matrix_divided.txt)

[3-say_my_name.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x07-python-test_driven_development/3-say_my_name.py) - a function that prints `My name is <first name> <last name>`
  - Prototype: `def say_my_name(first_name, last_name=""):`
  - `first_name` and `last_name` must be strings otherwise, raise a `TypeError` exception with the message `first_name must be a string` or `last_name must be a string`
  - **Test_Case:** [3-say_my_name.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x07-python-test_driven_development/tests/3-say_my_name.txt)

[4-print_square.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x07-python-test_driven_development/4-print_square.py) - a function that prints a square with the character `#`
  - Prototype: `def print_square(size):`
  - `size` is the size length of the square
  - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
  - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
  - if `size` is a float and is less than 0, raise a `TypeError` exception with the message `size must be an integer`
  - **Test_Case:** [4-print_square.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x07-python-test_driven_development/tests/4-print_square.txt)

[5-text_indentation.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x07-python-test_driven_development/5-text_indentation.py) - a function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`
  - Prototype: `def text_indentation(text):`
  - `text`must be a string, otherwise raise a `TypeError` exception with the message `text must be a string`
  - There should be no space at the beginning or at the end of each printed line
  - **Test_Case:** [5-text_indentation.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x07-python-test_driven_development/tests/5-text_indentation.txt)

[6-max_integer_test.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x07-python-test_driven_development/6-max_integer_test.py) - unittests for the function `def max_integer(list=[]):`
   - use the `unittest module`
   - test file should be python files (extension: `.py`)
   - test file should be executed by using this command: `python3 -m unittest tests.6-max_integer_test`

[100-matrix_mul.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x07-python-test_driven_development/100-matrix_mul.py) - a function that multiplies 2 matrices:
  - Prototype: `def matrix_mul(m_a, m_b):`
  - `m_a` and `m_b` must be validated with these requirements in this order
  - `m_a` and `m_b` must be an list of lists of integers or floats:
      - if `m_a` or `m_b` is not a list: raise a `TypeError` exception with the message `m_a must be a list` or `m_b must be a list`
      - if `m_a` or `m_b` is not a list of lists: raise a `TypeError` exception with the message `m_a must be a list of lists` or `m_b must be a list of lists`
      - if `m_a` or `m_b` is empty (it means: `= []` or `= [[]]`): raise a `ValueError` exception with the message `m_a can't be empty` or `m_b can't be empty`
      - if one element of those list of lists is not an integer or a float: raise a `TypeError` exception with the message `m_a should contain only integers or floats` or `m_b should contain only integers or floats`
      - if `m_a` or `m_b` is not a rectangle (all ‘rows’ should be of the same size): raise a `TypeError` exception with the message `each row of m_a must be of the same size` or `each row of m_b must be of the same size`
  - If `m_a` and `m_b` can’t be multiplied: raise a `ValueError` exception with the message `m_a and m_b can't be multiplied`
  - **Test_Case:** [100-matrix_mul.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x07-python-test_driven_development/tests/100-matrix_mul.txt)

[101-lazy_matrix_mul.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x07-python-test_driven_development/101-lazy_matrix_mul.py) -  a function that multiplies 2 matrices by using the module [NumPy](https://numpy.org/)
  - To install it: `pip3 install numpy==1.15.0`
      - Prototype: `def lazy_matrix_mul(m_a, m_b):`
  - **Test_Case:** [101-lazy_matrix_mul.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x07-python-test_driven_development/tests/101-lazy_matrix_mul.txt)
