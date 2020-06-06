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

    def to_json(self, attrs=None):
        """
            Returns the dictionary
        """
        if attrs is None:
            return self.__dict__
        else:
            dictn = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dictn[att] = self.__dict__[att]
            return dictn

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        """
        for i, j in json.items():
            setattr(self, i, j)
