#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    print(text)
    for i in text:
        if i in (".", "?", ":"):
            print("{:s}".format(i), end="\n\n")
        else:
            print("{:s}".format(i), end="")
