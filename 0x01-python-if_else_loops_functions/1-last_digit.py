#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    remainder = -1 * (abs(number) % 10)
else:
    remainder = number % 10
print(f"Last digit of {number} is", end=' ')
if remainder > 5:
    print(f"{remainder} and is greater than 5")
elif remainder == 0:
    print(f"{remainder} and is 0")
else:
    print(f"{remainder} and is less than 6 and not 0")
