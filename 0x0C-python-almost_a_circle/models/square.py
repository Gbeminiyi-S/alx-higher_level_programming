#!/usr/bin/python3
""" This module creates a class: Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines a new square """

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        name = "[Square] "
        a = str(self.id)
        b = str(self.x)
        c = str(self.y)
        d = str(self.width)
        return name + "(" + a + ") " + b + '/' + c + ' - ' + d

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the Square
        Args:
            *args (ints): New attribute values
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes
        """
        itr = 1

        if (args) and len(args):
            for arg in args:
                if itr == 1:
                    self.id = arg
                elif itr == 2:
                    self.size = arg
                elif itr == 3:
                    self.x = arg
                elif itr == 4:
                    self.y = arg
                itr += 1

        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """

        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
