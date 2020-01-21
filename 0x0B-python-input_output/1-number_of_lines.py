#!/usr/bin/python3
def number_of_lines(filename=""):
    n_line = 0
    with open(filename, mode='r', encoding='utf-8') as a_file:
        for a_line in a_file:
            n_line += 1
    return n_line
