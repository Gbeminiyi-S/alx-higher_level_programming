#!/usr/bin/python3
""" Module to create a function: append_after """


def append_after(filename="", search_string="", new_string=""):
    """  inserts a line of text to a file, after each line
         containing a specific string

    Args:
        filename (str): name of the file
        search_string (str): string to search for within the file
        new_string (str): string to insert
    """

    new_text = ""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            new_text += line
            if search_string in line:
                new_text += new_string
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(new_text)
