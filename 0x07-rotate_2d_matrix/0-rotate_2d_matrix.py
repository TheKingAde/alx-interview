#!/usr/bin/python3
"""
Function rotates a 2d matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
