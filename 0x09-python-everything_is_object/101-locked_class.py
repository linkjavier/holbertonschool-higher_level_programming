#!/usr/bin/python3
"""No class or object attribute"""


class LockedClass:
    """Only accepts attribute first_name  """
    __slots__ = 'first_name'
