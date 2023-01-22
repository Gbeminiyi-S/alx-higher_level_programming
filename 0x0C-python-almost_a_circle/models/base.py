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

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON strings representation of list_objs to a file

        Args:
            list_objs(list): a list of instances who inherits of Base
        """
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as f:
            if not list_objs:
                res = []
            else:
                res = [i.to_dictionary() for i in list_objs]
            f.write(Base.to_json_string(res))
