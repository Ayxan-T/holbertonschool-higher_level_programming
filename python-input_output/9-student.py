#!/usr/bin/python3
"""
    Module: 9-student
    This module is a part of the 'Python - Input/Output' project.
"""


class Student:
    """ A class Student that represents a student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        res = dict()
   	    for a in dir(obj):
            if a[:2] == "__":
                continue
            res[a] = getattr(obj, a)
        return res
