#!/usr/bin/pyhton3
""" lazy matrix mul module """
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Multiplication of two matrix
    Args:
    m_a: 1st matrix
    m_b: 2nd matrix
    Return: product of the two matrix """
    return (np.matmul(m_a, m_b))
