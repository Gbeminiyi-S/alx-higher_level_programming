#!/usr/bin/python3
""" Module to create a function: save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation """
    my_obj = json.dumps(my_obj)
    with open(filename, 'w') as f:
        f.write(my_obj)
