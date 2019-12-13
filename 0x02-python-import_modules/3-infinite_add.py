#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    i = len(sys.argv)
    if i == 1:
        print("0")
    else:
        i = 0
        for a in sys.argv:
            if a == sys.argv[0]:
                continue
            i += int(a)
        print("{:d}".format(i))
