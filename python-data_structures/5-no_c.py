#!/usr/bin/python3
# here goes your f comment

def no_c(my_string):
    indexes = []
    # for each char in my_string
        # if char is c or C
            # add its index to cC_indexes
    # for each index in cC_indexes
        # slice my_string in two parts, add them and assign it to my_string

    # return my_string

    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            indexes.append(i)

    k = 0
    for index in indexes:
        idx = index - k
        my_string = my_string[:idx] + my_string[(idx + 1):]
        k += 1

    return my_string
