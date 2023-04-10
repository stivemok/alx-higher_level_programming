#!/usr/bin/python3


""" MyList module """
class MyList(list):
    """ MyList class """
    def print_sorted(self):
        """
        public  instance method that prints the list(ascending sort)
        """
        print(sorted(self))

