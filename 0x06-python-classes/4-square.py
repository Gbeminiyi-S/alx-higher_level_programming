#!/usr/bin/python3
"""No module imported"""


class Square:
    """Defines a class: Square with a private attribute: size and checks Errors
       and returns the area of the square"""

    def __init__(self, size=0):
        self.size = size

    def area(self):
        return (pow(self.__size, 2))

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
