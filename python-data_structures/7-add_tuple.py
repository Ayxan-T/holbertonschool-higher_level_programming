#!/usr/bin/python3
# here goes your f comment

def add_tuple(tuple_a=(), tuple_b=()):
    sums = [0, 0]

    k = -1
    for item in tuple_a:
        if k == 1:
            break
        k += 1
        sums[k] += item
    k = -1
    for item in tuple_b:
        if k == 1:
            break
        k += 1
        sums[k] += item

    return tuple(sums)
