#!/usr/bin/python3
""" a module defining only one function """


def is_same_class(obj, a_class):
    """ a function that checks whether 'obj' is exactly an instance of 'a_class' or not """
    return isinstance(obj, a_class)
