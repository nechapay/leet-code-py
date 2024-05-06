import unittest
from lc_35_SearchInsertPosition import *


class TestSearchInsertPosition(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(searchInsert([1, 3, 5, 6], 5), 2)

    def test_case2(self):
        self.assertEqual(searchInsert([1, 3, 5, 6], 2), 1)

    def test_case3(self):
        self.assertEqual(searchInsert([1, 3, 5, 6], 7), 4)


if __name__ == '__main__':
    unittest.main(verbosity=2)
