#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 == {} or set_2 == {}:
        return {}

    return (set_1 - set_2) | (set_2 - set_1)
