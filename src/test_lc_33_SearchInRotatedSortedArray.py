import unittest
from lc_33_SearchInRotatedSortedArray import *


class TestSearchInRotatedSortedArray(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(search([4, 5, 6, 7, 0, 1, 2], 0), 4)

    def test_case2(self):
        self.assertEqual(search([4, 5, 6, 7, 0, 1, 2], 3), -1)

    def test_case3(self):
        self.assertEqual(search([1], 0), -1)

    def test_case4(self):
        self.assertEqual(search([], 0), -1)

    def test_case5(self):
        self.assertEqual(search([1], 1), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
