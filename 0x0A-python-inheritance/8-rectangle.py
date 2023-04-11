#!/usr/bin/python3
""" BaseGeometry module """


class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        """ public instance method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ public instance method
        Args:
        name: a string name of a parameter
        value: an integer parameter to validate
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Rectangle class inherits from BaseGeometry """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height
