#!/usr/bin/python3
"""Documentation square class"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Initializes class attribite
        Args:
        size(int): size of the square
        Raises:
        TypeError: value passed not an integer
        ValueError: value passed is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
