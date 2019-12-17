#!/usr/bin/python3
def no_c(my_string):
    cpstr = ""
    for i in my_string:
        if ord(i) != ord('c') and ord(i) != ord('C'):
            cpstr = cpstr + i

    return cpstr
