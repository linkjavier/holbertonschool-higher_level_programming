#!/usr/bin/python3
""" Function that returns True if the object is exactly
    an instance of the specified class ; otherwise False.
 """


def is_same_class(obj, a_class):
    """ Function that returns True if the object is exactly
        an instance of the specified class ; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) == a_class
