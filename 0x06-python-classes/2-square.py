#!/usr/bin/python3
"""Write an class Square that defines a square"""


class Square:
    """Square Class"""
    def __init__(self, size=0):
        """Initialize the object with size value"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
