#!/usr/bin/python3
def remove_char_at(str, n):
    if n is 0:
        s = str[1:]
    elif n is len(str) - 1:
        s = str[:-1]
    elif n < 0:
        s = str
    else:
        s = str[:n] + str[n + 1:]
    return s
