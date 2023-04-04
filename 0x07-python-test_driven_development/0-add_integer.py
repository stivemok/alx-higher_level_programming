#!/usr/bin/python3
""" add integer module """


def add_integer(a, b=98):
    """ adds two integers
    Args:
    a: first integer
    b: second integer
    return: addition of two integers"""

    if type(a) is not int and type(a) is not float:
        raise TypeError("a be must be integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
