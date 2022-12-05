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
	- The string `Last digit of`, followed by
  	- the `number`, followed by
	- the string `is`, followed by the last digit of `number`, followed by
		- if the last digit is greater than 5: the string `and is greater than 5`
		- if the last digit is 0: the string `and is 0`
		- if the last digit is less than 6 and not 0: the string `and is less than 6 and not 0`
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

[9-print_last_digit.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/9-print_last_digit.py) - a function that prints the last digit of a number

[10-add.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/10-add.py) - a function that adds two integers and returns the result

[11-pow.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/11-pow.py) - a function that computes `a` to the power of `b` and return the value

[12-fizzbuzz.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/12-fizzbuzz.py) - a function that prints the numbers from 1 to 100 separated by a space
- For multiples of three print `Fizz` instead of the number and for multiples of five print `Buzz`
- For numbers which are multiples of both three and five print `FizzBuzz`
- Each element should be followed by a space

[13-insert_number.c](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/13-insert_number.c) - a function in C that inserts a number into a sorted singly linked list

[100-print_tebahpla.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/100-print_tebahpla.py) - a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line

[101-remove_char_at.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/101-remove_char_at.py) - a function that creates a copy of the string, removing the character at the position `n` (not the Python way, the “C array index”)

[102-magic_calculation.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/102-magic_calculation.py) - a Python function `def magic_calculation(a, b, c):` that does exactly the same as the following Python bytecode:
```
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```
