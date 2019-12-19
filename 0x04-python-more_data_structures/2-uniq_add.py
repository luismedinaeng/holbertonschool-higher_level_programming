#!/usr/bin/python3
def uniq_add(my_list=[]):
    b = list(my_list)
    b.sort()
    return sum([b[i] if b[i] != b[i-1] else 0 for i in range(len(b))])
