#!/usr/bin/python3
"""
    Function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
        Function that appends a string at the end of a text file (UTF8)
        and returns the number of characters added
    """
    with open(filename, "a") as file:
        nb_char = file.write(str(text))
        return nb_char
