#!/usr/bin/python3
"""
    Module: 0-read_file
    This module is a part of the 'Python - Input/Output' project.
"""


def read_file(filename=""):
    """
        A function that reads a text file (UTF8) and prints it to stdout
        args:
            filename - name of the file, empty string by default
    """
    with open(filename) as f:
        for line in f:
            print(line, end="")
