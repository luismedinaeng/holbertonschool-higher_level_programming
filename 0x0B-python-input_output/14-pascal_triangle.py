#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]

    pascal = [[1], [1, 1]]
    for i in range(2, n):
        a_list = list(range(i + 1))
        for j in range(i + 1):
            if j == 0:
                a_list[j] = 1
            elif j == i:
                a_list[j] = 1
            else:
                a_list[j] = pascal[i - 1][j] + pascal[i - 1][j - 1]
        pascal.append(a_list)

    return pascal
