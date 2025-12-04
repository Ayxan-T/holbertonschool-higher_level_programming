#!/usr/bin/python3
# here goes your f comment

def multiple_returns(sentence):
    l = len(sentence)
    if l == 0:
        return (l, None)
    return (l, sentence[0])
