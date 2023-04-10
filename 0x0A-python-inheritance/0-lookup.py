#!/usr/bin/pyhton3
""" look up module """


def lookup(obj):
    """
    Args:
    obj: initial object
    Returns: the list of available
    attributes and methods of an object
    """
    list = (dir(obj))
    return list
