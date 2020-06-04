#!/usr/bin/python3
"""
    Function that returns the number of lines
    of a text file:
"""


def number_of_lines(filename=""):
    """
        Function that returns the number of lines
        of a text file:
    """
    with open(filename, 'r') as a_file:
        count = 0
        for line in a_file:
            count += 1
        return count
