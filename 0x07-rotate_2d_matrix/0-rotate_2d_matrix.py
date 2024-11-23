#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.

    Prototype: def rotate_2d_matrix(matrix):
    Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dimensions and will not be empty.

    """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):  # Only iterate for j > i and less than n
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
