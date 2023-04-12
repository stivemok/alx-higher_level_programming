#!/usr/bin/python3
"""pascal_triangle function"""

def pascal_triangle(n):
    if n <= 0:
        return []
    trgl = [[1]]
    while len(trgl) != n:
