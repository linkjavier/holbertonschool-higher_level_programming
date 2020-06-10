#!/usr/bin/python3
from models.base import Base
"""Rectangle Module"""


class Rectangle(Base):
    """class Rectangle - Base inherits"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Init Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return The Width value"""
        return self.__width

    @width.setter
    def width(self, width):
        """Set new Width value"""
        super().is_int("width", width)
        super().less_zero("width", width)
        self.__width = width

    @property
    def height(self):
        """Return The Height value"""
        return self.__height

    @height.setter
    def height(self, height):
        """Set new Width value"""
        super().is_int("height", height)
        super().less_zero("height", height)
        self.__height = height

    @property
    def x(self):
        """Return The x value"""
        return self.__x

    @x.setter
    def x(self, x):
        """Set new x value"""
        super().is_int("x", x)
        super().under_zero("x", x)
        self.__x = x

    @property
    def y(self):
        """Return y value"""
        return self.__y

    @y.setter
    def y(self, y):
        """Set new y value"""
        super().is_int("y", y)
        super().under_zero("y", y)
        self.__y = y

    def area(self):
        """Returns the Rectangle area."""
        return (self.__width * self.__height)

    def display(self):
        """ Prints in stdout the Rectangle instance
            with the character #
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """str"""
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args and (args != []):
            att = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, att[i], args[i])
        else:
            for j in kwargs:
                if hasattr(self, j):
                    setattr(self, j, kwargs[j])

    def to_dictionary(self):
        """Returns the Rectangle in a dictionary"""
        dict_rep = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return dict_rep
