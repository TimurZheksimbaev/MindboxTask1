import unittest
from Shape import *
class TestShapes(unittest.TestCase):
    def test_circle(self):
        c = Circle(5)
        self.assertAlmostEqual(c.area(), 78.53981633974483)

    def test_triangle(self):
        t = Triangle(3, 4, 5)
        self.assertEqual(t.area(), 6)
        self.assertTrue(t.is_right_angled())

if __name__ == '__main__':
    unittest.main()