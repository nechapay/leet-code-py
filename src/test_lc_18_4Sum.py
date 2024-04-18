import unittest
from lc_18_4Sum import *


class Test4Sum(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(
            fourSum([1, 0, -1, 0, -2, 2], 0), [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])

    def test_case2(self):
        self.assertEqual(fourSum([2, 2, 2, 2, 2], 8), [[2, 2, 2, 2]])


if __name__ == '__main__':
    unittest.main(verbosity=2)
