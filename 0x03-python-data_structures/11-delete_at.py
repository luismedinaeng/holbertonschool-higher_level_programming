#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        value = my_list[idx]
        for i in range(len(my_list) - 1, 0, -1):
            if i <= idx:
                my_list[i] = my_list[i - 1]
        my_list[0] = value
        my_list.remove(value)
        return my_list
