#!/usr/bin/python3
# here goes your f comment

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxint = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > maxint:
            maxint = my_list[i]
    return maxint
