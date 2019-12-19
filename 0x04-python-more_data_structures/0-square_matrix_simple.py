#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix == []:
        return matrix

    new_m = list([j**2 for j in i] for i in matrix)
    return new_m
