#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        remainder = abs(number) % 10
    else:
        remainder = number % 10
    print("{}".format(remainder), end='')
    return (remainder)
