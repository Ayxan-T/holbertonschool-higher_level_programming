#!/usr/bin/python3
"""
    Module: 7-add_item
    This module is a part of the 'Python - Input/Output' project.
"""

import os, sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

my_list = sys.argv[1:]
JSON_FILE = "add_item.json"
if os.path.exists(JSON_FILE):
    temp = load_from_json_file(JSON_FILE)
    my_list = temp + my_list
save_to_json_file(my_list, JSON_FILE)
