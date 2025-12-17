#!/usr/bin/python3
""" Module: task_00_basic_serialization
    This module is a part of the 'Python - Serialization' project.
"""
import json


def serialize_and_save_to_file(data, filename):
    """ A function that serializes and saves data to the specified file.
    input:
        data -- a python dictionary with data
        filename -- filename of the JSON file to be written to
    """
    json_str = json.dumps(data)
    with open(filename, 'w') as f:
        f.write(json_str)

def load_and_deserialize(filename):
    """ A function that loads and deserializes data from the specified file.
    input:
        filename -- filename of the JSON file 
    output:
        python_dictionary -- the deserialized python dictionary
    """
    with open(filename, 'r') as f:
        json_str = f.read()
    return json.loads(json_str)
