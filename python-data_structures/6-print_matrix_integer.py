#!/usr/bin/python3
# here goes your f comment

def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print()
        exit()
    for row in matrix:
        for element in row[:-1]:
            print("{:d}".format(element), end=" ")
        print("{:d}".format(row[-1]))
