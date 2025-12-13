#!/usr/bin/python3
"""
Module: 0-is_same_class
A module defining a single function to check for exact class instance.

This module is part of the Python - Inheritance project.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is **exactly** an instance of the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match against.

    Returns:
        bool: True if 'obj' is exactly an instance of 'a_class',
        False otherwise.
    """
    return type(obj) is a_class
