#!/usr/bin/pyhton3
""" inherits_from module """


def inherits_from(obj, a_class):
    """
    returns true if the oject is an instance of a class
    that inherited from the specified class; otherwise false
    """
    if issubclass(obj.__class__, a_class) and type(obj) != a_class:
        return True
    return False
