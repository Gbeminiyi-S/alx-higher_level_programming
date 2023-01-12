#!/usr/bin/python3
""" Module to check instance of a specified class """


def is_same_class(obj, a_class):
    """ checks if the object is exactly an instance
    of the specified class """

    return type(obj) == a_class
