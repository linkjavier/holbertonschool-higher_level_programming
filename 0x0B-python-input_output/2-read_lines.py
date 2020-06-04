#!/usr/bin/python3
"""
    Function that returns the number of lines
    of a text file:
"""


def read_lines(filename="", nb_lines=0):
    """
        Function that returns the number of lines
        of a text file:
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        lines = file.readlines()
        number_lines = len(lines)

        if nb_lines <= 0 or nb_lines > number_lines:
            for line in lines:
                print(line, end="")
        else:
            number_lines = 1
            for line in lines:
                print(line, end="")
                number_lines += 1
                if number_lines > nb_lines:
                    break
