#!/usr/bin/python3
""" This module creates a class: Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines a new square """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        name = "[Square] "
        a = str(self.id)
        b = str(self.x)
        c = str(self.y)
        d = str(self.width)
        return name + "(" + a + ") " + b + '/' + c + ' - ' + d
