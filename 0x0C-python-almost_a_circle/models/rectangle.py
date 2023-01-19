#!/usr/bin/python3
""" This module creates a class: Rectangle"""
from models.base import Base


class Rectangle(Base):
    """ Defines a new rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """ Returns the area of a rectangle """

        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with the character '#' """

        goRight = self.__x
        goDown = self.__y
        for i in range(goDown):
            print()
        for i in range(self.area()):
            if i and not (i % self.__width):
                print()
            if not (i % self.__width):
                for j in range(goRight):
                    print(' ', end='')
            print('#', end='')
        print()

    def __str__(self):
        name = "[Rectangle] "
        a = str(self.id)
        b = str(self.__x)
        c = str(self.__y)
        d = str(self.__width)
        e = str(self.__height)
        return name + "(" + a + ") " + b + '/' + c + ' - ' + d + '/' + e

    def update(self, *args, **kwargs):
        """ Updates the Rectangle.
        Args:
            *args (ints): New attribute values
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes
        """
        itr = 1

        if (args) and len(args):
            for arg in args:
                if itr == 1:
                    self.id = arg
                elif itr == 2:
                    self.__width = arg
                elif itr == 3:
                    self.__height = arg
                elif itr == 4:
                    self.__x = arg
                elif itr == 5:
                    self.__y = arg
                itr += 1

        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value
