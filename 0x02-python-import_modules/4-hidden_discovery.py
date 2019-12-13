#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import hidden_4
    for var in dir(hidden_4):
        if var[:2] == "__":
            continue
        print("{}".format(var))
