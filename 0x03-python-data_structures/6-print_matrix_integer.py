#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    else:
        for row in matrix:
            c = 1
            for col in row:
                print("{:d}".format(col), end=" " if c != len(row) else "\n")
                c += 1
