#!/usr/bin/python3
""" module to create a function: write_file """


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8) and returns
        the number of characters written
    """

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        return f.tell()
