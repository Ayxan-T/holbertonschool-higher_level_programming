#!/usr/bin/python3
""" Module: task_03_xml
    This module is a part of 'Python - Serialization' project
"""

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = SubElement(root, key)
        child.text = value

    tree = TreeElement(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    res = dict()
    for child in root:
        res[child.tag] = child.text
    
    return res
