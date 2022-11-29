#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_cpy = number
if number_cpy < 0:
	number_cpy *= -1
if (number_cpy % 10) > 5:
	print(f"Last digit of {number} is {number_cpy % 10} and is greater than 5")
elif (number_cpy % 10) == 0:
	print(f"Last digit of {number} is {number_cpy % 10} and is 0")
else:
	print(f"Last digit of {number} is {number_cpy % 10} and is less than 6 and not 0")
