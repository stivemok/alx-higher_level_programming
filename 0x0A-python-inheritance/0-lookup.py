#!/usr/bin/python3
""" lookup module """


def lookup(obj):
    """ Args:
    obj: initial object
    Return: the list of available attributes and methodes of an object
    """
    return (dir(obj))

