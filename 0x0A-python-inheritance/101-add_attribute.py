#!/usr/bin/python
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

    try:
        setattr(obj, name, value)
    except Exception:
        raise TypeError("can't add new attribute")
