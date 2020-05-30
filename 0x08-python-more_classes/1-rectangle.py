#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Rectangle class with width and height."""

    def __init__(self, width=0, height=0):
        """Rectangle instance.
        Args:
            width: width
            height: height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width
        Args:
            value: The width, positive int.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height
        Args:
            value: The height, positive int.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
