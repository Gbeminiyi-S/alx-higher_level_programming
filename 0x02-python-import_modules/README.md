# 0x02. Python - import & modules
An introductory project on:

- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function `dir()`
- How to prevent code in script from being executed when imported
- How to use command line arguments with Python programs
## Requirements
### Python Scripts
- Files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Codes are checked with the pycodestyle (version 2.8.*)
- All files are executable
## File Descriptions
### Mandatory
[0-add.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x02-python-import_modules/0-add.py) - a program that imports the function `def add(a, b)`: from the file [add_0.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x02-python-import_modules/test_files/add_0.py) and prints the result of the addition `1 + 2 = 3`
- the value `1` is assigned to a variable called `a`
- the value `2` is assigned to a variable called `b`
- the two variables as arguments when calling the functions `add` and `print`

[1-calculation.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x02-python-import_modules/1-calculation.py) - a program that imports functions from the file [calculator_1.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x02-python-import_modules/test_files/calculator_1.py), does some Maths, and prints the result.
- the value `10` is defined to a variable `a`
- the value `5` is defined to a variable `b`

[2-args.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x02-python-import_modules/2-args.py) - a program that prints the number of and the list of its arguments
- Number of argument(s) followed by `argument` (if number is one) or `arguments` (otherwise), followed by
- `:` (or `.` if no arguments were passed) followed by
- a new line, followed by (if at least one argument),
- one line per argument
  - the position of the argument (starting at 1) followed by :, followed by the argument value and a new line

[3-infinite_add.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x02-python-import_modules/3-infinite_add.py) - a program that prints the result of the addition of all arguments 

[4-hidden_discovery.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x02-python-import_modules/4-hidden_discovery.py) - a program that prints all the names defined by the compiled module [hidden_4.pyc](https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc)

[5-variable_load.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x02-python-import_modules/5-variable_load.py) - a program that imports the variable `a` from the file [variable_load_5.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x02-python-import_modules/test_files/variable_load_5.py) and prints its value

[100-my_calculator.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x02-python-import_modules/100-my_calculator.py) - a program that imports all functions from the file [calculator_1.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x02-python-import_modules/test_files/calculator_1.py) and handles basic operations

[101-easy_print.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x02-python-import_modules/101-easy_print.py) - a program that prints `#pythoniscool`, followed by a new line, in the standard output
- not allowed to use `print` or `eval` or `open` or `import sys`

[102-magic_calculation.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x02-python-import_modules/102-magic_calculation.py) - Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:
```
 3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (('add', 'sub'))
              6 IMPORT_NAME              0 (magic_calculation_102)
              9 IMPORT_FROM              1 (add)
             12 STORE_FAST               2 (add)
             15 IMPORT_FROM              2 (sub)
             18 STORE_FAST               3 (sub)
             21 POP_TOP

  4          22 LOAD_FAST                0 (a)
             25 LOAD_FAST                1 (b)
             28 COMPARE_OP               0 (<)
             31 POP_JUMP_IF_FALSE       94

  5          34 LOAD_FAST                2 (add)
             37 LOAD_FAST                0 (a)
             40 LOAD_FAST                1 (b)
             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             46 STORE_FAST               4 (c)

  6          49 SETUP_LOOP              38 (to 90)
             52 LOAD_GLOBAL              3 (range)
             55 LOAD_CONST               3 (4)
             58 LOAD_CONST               4 (6)
             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             64 GET_ITER
        >>   65 FOR_ITER                21 (to 89)
             68 STORE_FAST               5 (i)

  7          71 LOAD_FAST                2 (add)
             74 LOAD_FAST                4 (c)
             77 LOAD_FAST                5 (i)
             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             83 STORE_FAST               4 (c)
             86 JUMP_ABSOLUTE           65
        >>   89 POP_BLOCK

  8     >>   90 LOAD_FAST                4 (c)
             93 RETURN_VALUE

 10     >>   94 LOAD_FAST                3 (sub)
             97 LOAD_FAST                0 (a)
            100 LOAD_FAST                1 (b)
            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            106 RETURN_VALUE
            107 LOAD_CONST               0 (None)
            110 RETURN_VALUE
```
[103-fast_alphabet.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x02-python-import_modules/103-fast_alphabet.py) - a program that prints the alphabet in uppercase, followed by a new line
- not allowed to use:
  - any loops
  - any conditional statements
  - `str.join()`
  - any string literal
  - any system calls
