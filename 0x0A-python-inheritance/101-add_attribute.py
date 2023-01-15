#!/usr/bin/python3
"""This module creates a function: add_attribute"""


def add_attribute(obj, name, value):
    """ Adds a new attribute to an object if it’s possible

    Args:
        obj (any): the object
        name (str): the name of the attribute
        value (any): The value of attribute
    Raises:
        TypeError: if the attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
