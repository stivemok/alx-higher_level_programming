#!/usr/bin/pyhton3
""" look up module: returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    list = (dir(obj))
    return list
