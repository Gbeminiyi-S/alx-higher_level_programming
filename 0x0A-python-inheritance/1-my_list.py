#!/usr/bin/python3
""" Module to create inherited class """


class MyList(list):
    """ creates a new class, MyList that inherits from list """

    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        print(sorted(self))
        return sorted(self)
