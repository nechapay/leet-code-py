import unittest
from lc_15_3Sum import *


class Test3Sum(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(
            threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])

    def test_edge_case1(self):
        self.assertEqual(threeSum([0, 1, 1]), [])

    def test_edge_case2(self):
        self.assertEqual(threeSum([0, 0, 0]), [[0, 0, 0]])

    def test_edge_case3(self):
        self.assertEqual(threeSum([0, 0]), [])


if __name__ == '__main__':
    unittest.main(verbosity=2)
