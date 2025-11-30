#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if ord(c) <= ord('z') and ord(c) >= ord('a'):
            i = ord('A') + ord(c) - ord('a')
        else:
            i = ord(c)
        print("{:c}".format(i), end="")
    print()
