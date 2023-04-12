#!/usr/bin/python3
"""append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """
    filename: append_after_100.txt
    search_string: Python
    new_string: "C is fun!"
    """
    with open(filename) as r:
        text = ''
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w') as w:
        w.write(text)
