#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    res = dict()
    for key in a_dictionary.keys():
        res[key] = a_dictionary[key] * 2
    return res
