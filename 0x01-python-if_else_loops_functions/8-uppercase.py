#!/usr/bin/python3
def uppercase(str):
    for i in str + "\n":
        to_low = ord('a') - ord('A')
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            print("{}".format(chr(ord(i) - to_low)), end="")
        else:
            print("{}".format(chr(ord(i))), end="")
