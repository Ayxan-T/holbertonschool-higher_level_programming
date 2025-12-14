#!/usr/bin/python3
"""
    Module: 3-to_json_string
    This module is a part of the 'Python - Input/Output' project.
"""


import json


def to_json_string(my_obj):
    """
        A function that returns the JSON representation of an object (string).
        args:
            my_obj - the object to be serialized
        returns:
            JSON representation as a string
    """

    return json.dumps(my_obj)
