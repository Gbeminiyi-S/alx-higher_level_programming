# 0x00. Python - Hello, World

An introductory project on:
- How to use the Python interpreter
- How to print text and variables using print
- How to use strings
- What are indexing and slicing in Python
- How to check the code with pycodestyle
## Requirements
### Python Scripts
- Files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Codes are checked with the pycodestyle (version 2.8.*)
### Shell Scripts
- All scripts are tested on Ubuntu 20.04 LTS
- All scripts are exactly two lines long (wc -l file should print 2)
- All your files are executable
- `export PYFILE=main.py`
- `export PYCODE='print(f"Best School: {88+10}")'`
### C Scripts
- Files are compiled on Ubuntu 20.04 LTS using gcc, using the options `-Wall -Werror -Wextra -pedantic -std=gnu89`
- Codes are check with the Betty style using [betty-style.pl](https://github.com/holbertonschool/Betty/blob/master/betty-style.pl) and [betty-doc.pl](https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl)
## File Descriptions
### Mandatory
[0-run](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x00-python-hello_world/0-run) - a Shell script that runs a Python script. The Python file name will be saved in the environment variable `$PYFILE`.

[1-run_inline](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x00-python-hello_world/1-run_inline) - a Shell script that runs Python code. The Python code will be saved in the environment variable `$PYCODE`

[2-print.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x00-python-hello_world/2-print.py) - a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line

[3-print_number.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x00-python-hello_world/3-print_number.py) - Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable number, followed by `Battery street`, followed by a new line

[4-print_float.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x00-python-hello_world/4-print_float.py) - Complete the [source code](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py) in order to print the float stored in the variable number with a precision of 2 digits

[5-print_string.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x00-python-hello_world/5-print_string.py) - Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters

[6-concat.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x00-python-hello_world/6-concat.py) - Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py) to print `Welcome to Holberton School!`

[7-edges.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x00-python-hello_world/7-edges.py) - Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py)
- not allowed to use any loops or conditional statements
- `word_first_3` should contain the first 3 letters of the variable `word`
- `word_last_2` should contain the last 2 letters of the variable `word`
- `middle_word` should contain the value of the variable `word` without the first and last letters

[8-concat_edges.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x00-python-hello_world/8-concat_edges.py) - Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py) to print `object-oriented programming with Python`, followed by a new line.
- not allowed to use any loops or conditional statements
- program should be exactly 5 lines lon
- not allowed to create new variables
- not allowed to use string literals

[9-easter_egg.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x00-python-hello_world/9-easter_egg.py) -  Python script that prints “The Zen of Python”, by TimPeters, followed by a new line

[10-check_cycle.c](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x00-python-hello_world/10-check_cycle.c) - a function in C that checks if a singly linked list has a cycle in it
- Prototype: `int check_cycle(listint_t *list);`
- Return: Return: `0` if there is no cycle, `1` if there is a cycle
- [lists.h](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x00-python-hello_world/lists.h): header file

[100-write.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x00-python-hello_world/100-write.py) - a Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line

[101-compile](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x00-python-hello_world/101-compile) - a script that compiles a Python script file. The Python file name will be stored in the environment variable `$PYFILE`

[102-magic_calculation.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x00-python-hello_world/102-magic_calculation.py) - Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

```
 3           0 LOAD_CONST               1 (98)
             3 LOAD_FAST                0 (a)
	     6 LOAD_FAST                1 (b)
	     9 BINARY_POWER
	     10 BINARY_ADD
	     11 RETURN_VALUE
```
