#!/usr/bin/python3
"""Documentation for Square class"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Initialize a new square
        Args:
        size(int) : size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Return the sizeof the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the square with a value
        Arg: value the new size pf the square
        Raises:
        TypeError: when the value passed in is not an integer
        ValueError: when the value passed in is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the currunt square area"""
        area = self.__size ** 2
        return area
