#!/usr/bin/python3
def write_file(filename="", text=""):
    n_byt = 0
    with open(filename, mode="w", encoding="utf-8") as a_file:
        if text != "":
            n_byt = a_file.write(text)
    return n_byt
