#!/usr/bin/python3

if __name__ == "__main__":
    fun = __import__("add_0").add
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, fun(a, b)))
