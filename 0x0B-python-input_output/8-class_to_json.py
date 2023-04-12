#!/usr/bin/python3
"""class_to_json function"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    obj: an instance of a Class"""
    return obj.__dict__
