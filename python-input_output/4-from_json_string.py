#!/usr/bin/python3
"""
    Module: 4-from_json_string
    This module is a part of the 'Python - Input/Output' project.
"""
import json


def from_json_string(my_str):
    """
        A function that returns an object (Python data structure)
        represented by a JSON string.
        args:
            my_str - the string to be deserialized
        returns:
            pthon object
    """

    return json.loads(my_str)
