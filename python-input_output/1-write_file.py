#!/usr/bin/python3
"""
    Module: 1-write_file
    This module is a part of the 'Python - Input/Output' project.
"""


def write_file(filename="", text=""):
    """
        A function that writes a string to a text file (UTF8)
        and returns the number of characters written.
        args:
            filename - name of the file
            text - the string to be written
        returns:
            number of characters written
    """

    with open(filename, "w") as f:
        return f.write(text)
