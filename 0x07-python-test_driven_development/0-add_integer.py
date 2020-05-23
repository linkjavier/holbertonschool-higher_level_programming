#!/usr/bin/python3
"""add_integer() adds 2 numbers.
     Args:
          a: int or float
          b: int or float
"""


def add_integer(a, b=98):
    """Raises:
          TypeError: int or float only.
       Return: a + b"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return a + b
