#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    b_list = list(my_list)
    for i in range(len(my_list)):
        b_list[i] = True if my_list[i] % 2 == 0 else False

    return b_list
