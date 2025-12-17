#!/usr/bin/python3
""" Module: task_01_pickle
    This module is a part of the 'Python - Serialization' project.
"""
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("""Name: {}
        Age: {}
        Is Student: {}""".format(self.name, self.age, self.is_student))

    def serialize(self, filename):
        pickled_obj = pickle.dumps(self)
        with open(filename, "wb") as f:
            f.write(pickled_obj)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                pickled_obj = f.read()
        except Exception as e:
                return None

        try:
            py_obj = pickle.loads(pickled_obj)
        except Exception:
            return None
        return py_obj
