import algebra
import unittest

class TestAlgebra(unittest.TestCase):

    def test_triangle_area_normal(self):
        self.assertEqual(algebra.area_triangle(20, 30), 300.0)
        self.assertEqual(type(algebra.area_triangle(20, 30)), float)

    def test_triangle_area_bad_arguments_and_errors(self):
        with self.assertRaises(TypeError):
            algebra.area_triangle(10)
        with self.assertRaises(TypeError):
            algebra.area_triangle(10, 20, 30)
        with self.assertRaises(TypeError):
            algebra.area_triangle(10, 'hello')
        with self.assertRaises(TypeError):
            algebra.area_triangle('hello', 10)
        with self.assertRaises(ValueError):
            algebra.area_triangle(-5, 10)

if __name__=='__main__':
    unittest.main()
