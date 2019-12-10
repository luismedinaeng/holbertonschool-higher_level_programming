#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        s = "\n" if i == len(str) - 1 else ""
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            print(chr(ord(str[i]) - (ord('a') - ord('A'))), end=s)
        else:
            print(chr(ord(str[i])), end=s)
