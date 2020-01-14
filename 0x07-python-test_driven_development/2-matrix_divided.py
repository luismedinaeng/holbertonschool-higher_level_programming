#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ Divide the elements of the matrix
    """
    if type(matrix) != list or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) " + \
                        "of integers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by 0")
    row_len = -1
    new_matrix = matrix[:]
    for i in range(len(matrix)):
        row = matrix[i]
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists) " + \
                            "of integers/floats")
        if row_len == -1:
            row_len = len(row)
        else:
            if row_len != len(row):
                raise TypeError("Each row of the matrix must have the same size")
        new_matrix[i] = row[:]
        for j in range(len(row)):
            elem = row[j]
            if type(elem) != int and type(elem) != float:
                raise TypeError("matrix must be a matrix (list of lists) " + \
                                "of integers/floats")
            new_matrix[i][j] = round(row[j]/div, 2)

    return new_matrix
