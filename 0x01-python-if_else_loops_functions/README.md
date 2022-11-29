# 0x01. Python - if/else, loops, functions
An introductory project on:

- Why indentation is so important in Python
- How to use the if, if ... else statements
- How to use comments
- How to affect values to variables
- How to use the while and for loops
- How to use the break and continues statements
- How to use else clauses on loops
- What does the pass statement do, and when to use it
- How to use range
- What is a function and how do you use functions
- What does return a function that does not use any return statement
- Scope of variables
- What’s a traceback
- What are the arithmetic operators and how to use them
## Requirements
### Python Scripts
- Files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Codes are checked with the pycodestyle (version 2.8.*)
### C Scripts
- Files are compiled on Ubuntu 20.04 LTS using gcc, using the options `-Wall -Werror -Wextra -pedantic -std=gnu89`
- Codes are check with the Betty style using [betty-style.pl](https://github.com/holbertonschool/Betty/blob/master/betty-style.pl) and [betty-doc.pl](https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl)
## File Descriptions
### Mandatory
[0-positive_or_negative.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/0-positive_or_negative.py) - This program assigns a random signed number to the variable `number` each time it is executed. Complete the [source code](https://github.com/holbertonschool/0x01.py/blob/master/0-positive_or_negative_py) in order to print whether the number stored in the variable `number` is positive or negative

- The output of the program should be:
  - The number, followed by
  	- if the `number` is greater than 0: `is positive`
	- if the `number` is 0: `is zero`
	- if the `number` is less than 0: `is negative`
  - followed by a new line

[1-last_digit.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/1-last_digit.py) - This program will assign a random signed number to the variable `number` each time it is executed. Complete the [source code](https://github.com/holbertonschool/0x01.py/blob/master/1-last_digit_py) in order to print the last digit of the `number` stored in the variable `number`

- The output of the program should be:
  - The string Last digit of, followed by
  	- the `number`, followed by
	- the string is, followed by the last digit of `number`, followed by
	  - if the last digit is greater than 5: the string `and is greater than 5`
	- if the number is less than 0: is negative
  - followed by a new line
[2-print_alphabet.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/2-print_alphabet.py) - a program that prints the `ASCII` alphabet, except 'q' and 'e'  in lowercase, not followed by a new line

[3-print_alphabt.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/3-print_alphabt.py) - a program that prints the `ASCII` alphabet, in lowercase, not followed by a new line

[4-print_hexa.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/4-print_hexa.py) -  a program that prints all numbers from `0` to `98` in decimal and in hexadecimal

[5-print_comb2.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/5-print_comb2.py) - a program that prints numbers from `0` to `99`.

[6-print_comb3.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/6-print_comb3.py) - a program that prints all possible different combinations of two digits.

[7-islower.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/7-islower.py) - a function that checks for lowercase character.
- not allowed to use `str.lower()` and `str.isupper()`

[8-uppercase.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/8-uppercase.py) - a function that prints a string in uppercase followed by a new line
- not allowed to use `str.lower()` and `str.isupper()`
