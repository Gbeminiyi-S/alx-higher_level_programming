#!/usr/bin/python3
""" This module creates a class: Base """
import json


class Base:
    """ This creates the base class for other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
