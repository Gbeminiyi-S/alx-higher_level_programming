#!/usr/bin/python3
""" Module to create a function: save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation """

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
