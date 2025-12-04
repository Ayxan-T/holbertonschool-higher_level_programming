#!/usr/bin/python3
# hello world

def square_matrix_simple(matrix=[]):
    res = []
    for row in matrix:
        my_row = []
        for elm in row:
            my_row.append(elm**2)
        res.append(my_row)
    return res
