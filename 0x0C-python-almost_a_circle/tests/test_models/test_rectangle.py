#!/usr/bin/python3
"""unittest for rectangle"""
import unittest
from models import rectangle
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """unit test of Rectangle class"""
    def test_documentation(self):
        self.assertTrue(len(rectangle.__doc__) > 0)
        self.assertTrue(len(Rectangle.__doc__) > 0)
        self.assertTrue(len(Rectangle.area.__doc__) > 0)
        self.assertTrue(len(Rectangle.display.__doc__) > 0)
        self.assertTrue(len(Rectangle.update.__doc__) > 0)
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) > 0)

    def test_getter_setter(self):
        """Test setter and getter"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(1, 2, 3, 4,)
        self.assertEqual(r3.id, 3)

        r4 = Rectangle(5, 2, 1, 1)
        self.assertEqual(r4.id, 4)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 0)

        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)

        self.assertEqual(r4.width, 5)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 1)
        self.assertEqual(r4.y, 1)

    def test_area_rectangle(self):
        Base._Base__nb_objects = 0

        r1 = Rectangle(2, 2)
        self.assertEqual(r1.area(), 4)

        r2 = Rectangle(10, 2)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(4, 6, 0, 0, 12)
        self.assertEqual(r3.area(), 24)

    def test_update_rect_args_orig(self):
        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_rect_1args(self):
        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_rect_2args(self):
        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 10, 10, 10, 89)
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_rect_kwargs(self):
        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_rect_1kwarg(self):
        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/1")

    def test_update_rect_2kwarg(self):
        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 1, 10, 10, 1)
        r1.update(width=1, x=2)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 2/10 - 1/1")

    def test_setter_width_type(self):
        Base._Base__nb_objects = 0

        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, [1, 2], 2)
        self.assertRaises(TypeError, Rectangle, (1, 2), 2)
        self.assertRaises(TypeError, Rectangle, 12.5, 2)
        self.assertRaises(TypeError, Rectangle, {1, 2}, 2)
        self.assertRaises(TypeError, Rectangle, float('inf'), 2)
        self.assertRaises(TypeError, Rectangle, float('NaN'), 2)

    def test_setter_width_zero_neg(self):
        Base._Base__nb_objects = 0

        self.assertRaises(ValueError, Rectangle, 0, 12)
        self.assertRaises(ValueError, Rectangle, -5, 12)

    def test_setter_height_type(self):
        Base._Base__nb_objects = 0

        self.assertRaises(TypeError, Rectangle, 2, [1, 2])
        self.assertRaises(TypeError, Rectangle, 2, (1, 2))
        self.assertRaises(TypeError, Rectangle, 2, 12.5)
        self.assertRaises(TypeError, Rectangle, 2, {1, 2})
        self.assertRaises(TypeError, Rectangle, 2, float('inf'))
        self.assertRaises(TypeError, Rectangle, 2, float('NaN'))

    def test_setter_height_zero_neg(self):
        Base._Base__nb_objects = 0

        self.assertRaises(ValueError, Rectangle, 12, 0)
        self.assertRaises(ValueError, Rectangle, 12, -5)

    def test_setter_x_type(self):
        Base._Base__nb_objects = 0

        self.assertRaises(TypeError, Rectangle, 1, 2, [1, 2], 2)
        self.assertRaises(TypeError, Rectangle, 1, 2, (1, 2), 2)
        self.assertRaises(TypeError, Rectangle, 1, 2, 12.5, 2)
        self.assertRaises(TypeError, Rectangle, 1, 2, {1, 2}, 2)
        self.assertRaises(TypeError, Rectangle, 1, 2, float('inf'), 2)
        self.assertRaises(TypeError, Rectangle, 1, 2, float('NaN'), 2)

    def test_setter_x_neg(self):
        Base._Base__nb_objects = 0

        self.assertRaises(ValueError, Rectangle, 1, 2, -5, 2)

    def test_setter_y_type(self):
        Base._Base__nb_objects = 0

        self.assertRaises(TypeError, Rectangle, 1, 2, 2, [1, 2])
        self.assertRaises(TypeError, Rectangle, 1, 2, 2, (1, 2))
        self.assertRaises(TypeError, Rectangle, 1, 2, 2, 12.5)
        self.assertRaises(TypeError, Rectangle, 1, 2, 2, {1, 2})
        self.assertRaises(TypeError, Rectangle, 1, 2, 2, float('inf'))
        self.assertRaises(TypeError, Rectangle, 1, 2, 2, float('NaN'))

    def test_setter_y_neg(self):
        Base._Base__nb_objects = 0

        self.assertRaises(ValueError, Rectangle, 1, 2, 2, -5)

    def test_to_dictionary_rect(self):
        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        expected_dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r1_dictionary, expected_dict)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 1/9 - 10/2")

        r1.update(x=10, y=10, id=10, height=10, width=10)
        r1_dictionary = r1.to_dictionary()
        expected_dict = {'x': 10, 'y': 10, 'id': 10, 'height': 10, 'width': 10}
        self.assertEqual(r1_dictionary, expected_dict)
        self.assertEqual(r1.__str__(), "[Rectangle] (10) 10/10 - 10/10")


if __name__ == '__main__':
    unittest.main()
