#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    i = len(sys.argv)
    if i == 1:
        print("0 arguments.")
    else:
        print("{:d} {}".format(i - 1, "argument:" if i == 2 else "arguments:"))
        i = 0
        for a in sys.argv:
            i += 1
            if i == 1:
                continue
            print("{:d}: {}".format(i - 1, a))
