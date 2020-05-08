#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in range(0, len(matrix)):
        new.append(list(map(modpow, matrix[i])))
    return (new)


def modpow(x):
    return (x ** 2)
