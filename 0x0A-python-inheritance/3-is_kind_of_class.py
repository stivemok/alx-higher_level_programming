#!/usr/bin/python3
""" is_kind_of_class module """


def is_kind_of_class(obj, a_class):
    """
    returns true if the object is an instance of,
    or inherited from specified class; otherwise false
    """
    if isinstance(obj, a_class):
        return True
    return False
