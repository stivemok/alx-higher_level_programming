#!/usr/bin/python3
""" is_same_class module """


def is_same_class(obj, a_class):
    """
    returns true if the object is exactly an instance
    of the specified class otherwise false
    """
    if type(obj) == a_class:
        return True
    return False
