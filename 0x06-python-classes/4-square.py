#!/usr/bin/python3
"""Write an class Square that defines a square"""


class Square:
    """Square Class"""
    def __init__(self, size=0):
        """Initialize the object with size value"""
        self.__size = size

    @property
    def size(self):
        """ Get the size"""
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Function that returns the area of the Square"""
        return self.__size*self.__size
