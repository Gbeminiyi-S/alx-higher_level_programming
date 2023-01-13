#!/usr/bin/python3
""" Module that creates a subclass: Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ defines a subclass: Square """

    def __init__(self, size):
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        """ returns the area of the square """

        return pow(self.__size, 2)
