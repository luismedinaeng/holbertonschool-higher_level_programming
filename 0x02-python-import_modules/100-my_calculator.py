#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    args = sys.argv
    i = len(args)
    if i != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    op = ops.get(args[2])

    if op is None:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(args[1])
    b = int(args[3])
    print("{:d} {} {:d} = {:d}".format(a, args[2], b, op(a, b)))
