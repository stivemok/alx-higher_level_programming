#!/usr/bin/python3
""" unit test for max integer """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ TsetMaxInteger class """

    def test_posotive(self):
        """ tests if the function gives the highest positive integer """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative(self):
        """ tests if the function gives the highest negative integer """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_positive_float(self):
        """ tests if the function gives the highest positive float """
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_negative_float(self):
        """ tests if the function gives the highest negative float """
        self.assertEqual(max_integer([-1.1, -2.2, -3.3, -4.4]), -1.1)

    def test_string(self):
        """ tests list of strings """
        self.assertEqual(max_integer(["school", "is", "cool"]), "school")

    def test_empty_string(self):
        """ tests an empty string """
        self.assertEqual(max_integer(""), None)

    def test_char(self):
        """ tests list of characters """
        self.assertEqual(max_integer(['s', 'c', 'h', 'o', 'l']), 's')

    def test_empty_list(self):
        """ tests an empty list """
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unitest.main()
