#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_key = None
    max_value = 0
    for key in a_dictionary.keys():
        if a_dictionary[key] > max_value:
            max_key = key
            max_value = a_dictionary[key]
    return max_key
