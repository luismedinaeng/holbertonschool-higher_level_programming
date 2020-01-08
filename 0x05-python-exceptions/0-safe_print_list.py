#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        c = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            c = c + 1
            if c >= x:
                break
    except IndexError:
        pass
    print("")
    return c
