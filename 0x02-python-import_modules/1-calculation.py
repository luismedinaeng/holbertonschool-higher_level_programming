#!/usr/bin/python3

if __name__ == "__main__":
    cal = __import__("calculator_1")
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, cal.add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, cal.sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, cal.mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, cal.div(a, b)))
