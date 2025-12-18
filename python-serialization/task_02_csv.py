#!/usr/bin/python3 
""" Module: task_00_basic_serialization
    This module is a part of the 'Python - Serialization' project.
"""

import csv
import json


def convert_csv_to_json(csv_file):
    """ A function that converts a CSV file to a JSON file. """
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        print(reader)
        # json_obj = [row for row in reader]
        
