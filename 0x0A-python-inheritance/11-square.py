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
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """ Square class inherits from Reclangle """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
