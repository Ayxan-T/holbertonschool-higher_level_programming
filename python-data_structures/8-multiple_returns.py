#!/usr/bin/python3
# here goes your f comment

def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        return (length, None)
    return (length, sentence[0])
