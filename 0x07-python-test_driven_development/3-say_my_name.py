#!/usr/bin/python3
""" say_my_name module """


def say_my_name(first_name, last_name=""):
    """ prints first name and last name
    Args:
    first_name: first string
    second_name: second_string
    """
    if type(first_name) is not str:
        raise TypeError("first name must be a string")
    if type(last_name) is not  str:
        raise TypeError("last name must be a string")
    print("My name is {} {}".format(first_name, last_name))
