#!/usr/bin/python3
""" write_file function """


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8) and
    returns the number of characters written
    filename: name of the file
    text: text to writein the file
    """
    with open(filename,'w', encoding='utf-8') as f:
        return f.write(text)
