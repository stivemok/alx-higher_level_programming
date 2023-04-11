#!/usr/bin/python3
""" MyInt module """


class MyInt(int):
    """ MyInt class """
    def __init__(self, value):
        if type(value) is not int:
            raise TypeError("value must be an integer")
        self.value = value

    def __ne__(self, value):
        return self.real == value

    def __eq__(self, value):
        return self.real != value
