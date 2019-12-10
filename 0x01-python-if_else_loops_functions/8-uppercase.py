#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        s = "\n" if i == len(str) - 1 else ""
        i = str[i]
        to_low = ord('a') - ord('A')
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            print("{}".format(chr(ord(i) - to_low)), end=s)
        else:
            print("{}".format(chr(ord(i))), end=s)
