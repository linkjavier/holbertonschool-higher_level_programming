#!/usr/bin/python3
"""matrix_divided() - Divides all elements of a matrix
     Args:
          matrix: A list of lists of integers or floats.
          div: A number (integer or float)
"""


def matrix_divided(matrix, div):
    """Raises:
          TypeError: matrix must be a matrix
          TypeError: Each row of the matrix must be of the same size
          TypeError: div must be a number (integer or float)
          TypeError: div can’t be equal to 0
       Return: new_matrix"""
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) is 0:
        raise TypeError(error)
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(error)
        if len(matrix[0]) is not len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(error)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    return[[round(j / div, 2) for j in i] for i in matrix]
