#!/usr/bin/python3
""" append_write function """


def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8) and
    returns the number of characters added
    filename: name of the file
    text: text to append to the file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
