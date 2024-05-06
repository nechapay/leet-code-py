import unittest
from lc_34_FindFirstAndLastInSortedArray import *


class TestFindFirstAndLastInSortedArray(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4])

    def test_case2(self):
        self.assertEqual(searchRange([5, 7, 7, 8, 8, 10], 6), [-1, -1])

    def test_case3(self):
        self.assertEqual(searchRange([], 0), [-1, -1])

    def test_case4(self):
        self.assertEqual(searchRange([0, 0, 0, 0, 0, 0, 0], 0), [0, 6])

    def test_case5(self):
        self.assertEqual(searchRange([1, 3], 1), [0, 0])


if __name__ == '__main__':
    unittest.main(verbosity=2)
