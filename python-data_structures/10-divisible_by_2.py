#!/usr/bin/python3
# here goes your f comment

def divisible_by_2(my_list=[]):
    res = []
    for item in my_list:
        res.append(item % 2 == 0)
    return res
