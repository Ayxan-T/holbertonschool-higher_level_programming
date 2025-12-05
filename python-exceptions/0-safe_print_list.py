#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for i in range(x):
        k = 0
        try:
            print("{:d}".format(my_list[i]), end="")
            k += 1
        except ValueError:
            pass
    print()
    return k
