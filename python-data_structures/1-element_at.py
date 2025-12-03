#!/usr/bin/python3
# just a random comment


def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
