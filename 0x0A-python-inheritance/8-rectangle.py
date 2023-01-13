#!/usr/bin/python3
""" Module that creates a class: BaseGeometry """


class BaseGeometry:
    """ defines the class: BaseGeometry """

    def area(self):
        """ returns the area """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validates value """

        if type(value) != int:
            raise TypeError(name + ' must be an integer')

        if value <= 0:
            raise ValueError(name + ' must be greater than 0')


class Rectangle(BaseGeometry):
    """ defines a Class: Rectangle"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
