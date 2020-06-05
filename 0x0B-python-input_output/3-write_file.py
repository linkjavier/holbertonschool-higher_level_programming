#!/usr/bin/python3
"""
    function that writes a string to a text file (UTF8)
    and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """
        function that writes a string to a text file (UTF8)
        and returns the number of characters written:
    """
    with open(filename, "w") as file:
        nb_char = file.write(str(text))
        return nb_char
