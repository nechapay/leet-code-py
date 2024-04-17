import unittest
from lc_11_ContainerWithMostWater import *


class TestAddTwoNumbers(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_edge_case1(self):
        self.assertEqual(maxArea([1, 1]), 1)

    def test_edge_case2(self):
        self.assertEqual(maxArea([]), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
