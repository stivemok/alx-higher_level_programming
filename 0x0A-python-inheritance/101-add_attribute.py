#!/usr/bin/python3
""" Adds a new attribute to an object """


def add_attribute(obj, attribute, value):
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
