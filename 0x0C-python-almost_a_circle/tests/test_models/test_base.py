#!/usr/bin/python3
"""unittest for base"""
import unittest
from models import base
from models.base import Base



class TestBaseClass(unittest.TestCase):
    """unit test of base class"""
    def test_documentation(self):
        self.assertTrue(len(base.__doc__) > 0)

    def test_Base_doc(self):
        self.assertTrue(len(Base.__doc__) > 0)

    def test_to_json_string_doc(self):
        self.assertTrue(len(Base.to_json_string.__doc__) > 0)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_save_to_file_doc(self):
        self.assertTrue(len(Base.save_to_file.__doc__) > 0)

    def test_from_json_string(self):
        self.assertTrue(len(Base.from_json_string.__doc__) > 0)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_create(self):
        self.assertTrue(len(Base.create.__doc__) > 0)

    def test_load_from_file(self):
        self.assertTrue(len(Base.load_from_file.__doc__) > 0)

    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

if __name__ == '__main__':
    unittest.main()
