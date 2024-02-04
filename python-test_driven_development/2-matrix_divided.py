#!/usr/bin/python3
"""
function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    matrix must be a list of lists of integers or floats
    Each row of the matrix must be of the same size
    div must be a number (integer or float)
    div can not be equal to 0
    """

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    result = [[round(elem / div, 2) for elem in row] for row in matrix]
    return result
