#!/usr/bin/python3
# just a random comment

def new_in_list(my_list, idx, element):
    replace = False
    if idx >= 0 and idx < len(my_list):
        replace = True

    new_list = []
    for i in range(0, len(my_list)):
        if i == idx:
            if replace:
                new_list.append(element)
        else:
            new_list.append(my_list[i])

    return new_list
