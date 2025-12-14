#!/usr/bin/python3
"""
    Module: 6-load_from_json_file
    This module is a part of the 'Python - Input/Output' project.
"""
import json


def load_from_json_file(filename):
    """
        A function that creates an Object from a JSON file.
        args:
            filename - the text file containing JSON data.
        returns:
            the create python object
    """
    with open(filename) as f:
        my_str = f.read()
        return json.loads(my_str)
