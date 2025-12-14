#!/usr/bin/python3
"""
    Module: 2-append_write
    This module is a part of the 'Python - Input/Output' project.
"""


def append_write(filename="", text=""):
    """
        A function that appends a string at the end of a text file (UTF8)
        and returns the number of characters added.
        args:
            filename - name of the file
            text - the string to be appended
        returns:
            number of characters appended
    """

    with open(filename, "a") as f:
        return f.write(text)
