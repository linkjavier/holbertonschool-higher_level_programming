#!/usr/bin/python3
"""Write an class Square that defines a square"""


class Square:
    """Square Class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the object with size value"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ Returns the position value"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position value of the square"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Function that returns the area of the Square"""
        return self.__size*self.__size

    def my_print(self):
        """print the square with #"""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
