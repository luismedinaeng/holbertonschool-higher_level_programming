#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    file_hid = __import__("hidden_4")
    for var in dir(file_hid):
        if var[:2] == "__":
            continue
        print("{}".format(var))
