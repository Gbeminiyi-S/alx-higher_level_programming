#!/usr/bin/python3
""" Module that creates a class: BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ defines a subclass: Rectangle """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ computes the area of the rectangle """

        return self.__width * self.__height

    def __str__(self):
        string = '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
        return string
