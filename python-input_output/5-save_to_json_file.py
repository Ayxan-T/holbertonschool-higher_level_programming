#!/usr/bin/python3
"""
    Module: 5-save_to_json_file
    This module is a part of the 'Python - Input/Output' project.
"""
import json


def save_to_json_file(my_obj, filename):
    """
        A function that writes an Object to a text file,
        using a JSON representation.
        args:
            my_obj - the object to be serialized
            filename - the text file to be written to
    """
    my_str = json.dumps(my_obj)
    with open(filename, "w"):
        f.write(my_str)
