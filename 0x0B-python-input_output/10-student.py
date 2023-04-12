#!/usr/bin/python3
"""Student module"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """public instance attributes:
        first_name, last_name, age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """public method :
        retrieves a dictionary representation of a student instance
        attrs: list of strings
        """
        if(type(attrs) != list):
            return self.__dict__
        for var in attrs:
            if(type(var) != str):
                return self.__dict__
        str_dict = {}
        for string in attrs:
            if string in self.__dict__.keys():
                str_dict[string] = self.__dict__[string]
        return str_dict
