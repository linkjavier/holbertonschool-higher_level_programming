#!/usr/bin/python3
"""
class Student
"""


class Student():
    """
    Public Attributes:
        first_name
        last_name
        age
    Public Methods:
        to_json: retrieves its dictionary representation
        of a Student instance
    """
    def __init__(self, first_name, last_name, age):
        """
            Instance student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            Returns the dictionary
        """
        return self.__dict__
