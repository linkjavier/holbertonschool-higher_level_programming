#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Rectangle class with width and height."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Rectangle instance.
        Args:
            width: width
            height: height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Returns the area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """returns rectangle with # """
        insert = ""
        if (self.__width == 0 or self.__height == 0):
            return insert
        for i in range(self.__height):
            for j in range(self.__width):
                insert += str(self.print_symbol)
            if (i != self.__height - 1):
                insert += '\n'
        return insert

    def __repr__(self):
        """Apropiate string of rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes Rectangles."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
