#!/usr/bin/python3
""" Adds a new attribute to an object """


def add_attribute(obj, attribute, value):
    """
    obj: object to add attribute
    attribute: attribute to add to an object
    value: valuse of the attribute
    """
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
