#!/usr/bin/python3
""" This module creates a class: MyInt """


class MyInt(int):
    """ Returns the inverse of '==' and '!=' operators """

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
