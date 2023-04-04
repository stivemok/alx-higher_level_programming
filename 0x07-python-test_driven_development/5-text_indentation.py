#!/usr/bin/python3
""" text indentation module """


def text_indentation(text):
    """ prints a text with 2 new line after '.', '?', ':'
    Args:
    text: a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1
    while i < len(text):
        print(text[i], end='')
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in '.?:':
                print('\n')
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
