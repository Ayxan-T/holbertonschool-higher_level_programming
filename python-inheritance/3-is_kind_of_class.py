#!/usr/bin/python3
"""
Module: 3-is_kind_of_class
A module defining a single function to check for class instance.

This module is part of the Python - Inheritance project.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of the specified
    class or any of its subclasses.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match against.

    Returns:
        bool: True if 'obj' is an instance of
        'a_class' or any of subclasses of 'a_class',
        False otherwise.
    """
    return isinstance(obj, a_class)
