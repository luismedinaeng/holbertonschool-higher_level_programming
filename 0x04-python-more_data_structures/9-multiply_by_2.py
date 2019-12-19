#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return a_dictionary
    ks = list(a_dictionary.keys())
    vs = list(a_dictionary.values())
    dc = a_dictionary.copy()
    for i, j in zip(ks, vs):
        dc[i] = j * 2
    return dc
