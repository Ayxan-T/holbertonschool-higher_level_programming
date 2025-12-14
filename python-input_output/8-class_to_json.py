#!/usr/bin/python3
"""
    Module: 8-class_to_json
    This module is a part of the 'Python - Input/Output' project.
"""


def class_to_json(obj):
    """ A  function that returns the dictionary description
    with simple data structure (list, dictionary, string, integer
    and boolean) for JSON serialization of an object.

    args:
        obj -- an instance of a class
    returns:
        serialized dictionary form of obj
    """

    res = dict()
    for a in dir(obj):
        if a[:2] == "__":
            continue
        res[a] = obj.getattr(a)
    return res
