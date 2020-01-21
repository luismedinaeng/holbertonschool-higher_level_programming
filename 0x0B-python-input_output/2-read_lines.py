#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    n_line = 0
    with open(filename, mode='r', encoding='utf-8') as a_file:
        if nb_lines <= 0:
            print(a_file.read(), end="")
        else:
            for a_line in a_file:
                print(a_line, end="")
                n_line += 1
                if n_line >= nb_lines:
                    break
