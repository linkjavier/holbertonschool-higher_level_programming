#!/usr/bin/python3
""" clear
    Function that reads a text file (UTF8)
    and prints it to stdout:
"""


def read_file(filename=""):
    """
        Function that reads a text file (UTF8)
        and prints it to stdout:
    """
    with open(filename, "encoding=utf8") as a_file:
        print(a_file.read())
    a_file.close
