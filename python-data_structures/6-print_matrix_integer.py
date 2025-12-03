#!/usr/bin/python3
# here goes your f comment

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            print("{:d}".format(element), end=" ")
        print()
