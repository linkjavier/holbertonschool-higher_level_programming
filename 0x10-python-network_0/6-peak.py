#!/usr/bin/python3
""" Program that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """
        Function that finds a peak in a list of unsorted integers.
    """
    lenght = len(list_of_integers)
    if lenght is 0:
        return None
    peak = check_side(list_of_integers, 0, lenght - 1)
    return list_of_integers[peak]


def check_side(a, min, max):
    """
        Function to search each side
    """
    if min >= max:
        return min
    half = ((max - min) // 2) + min
    if a[half] > a[half + 1]:
        return check_side(a, min, half)
    else:
        return check_side(a, half + 1, max)
