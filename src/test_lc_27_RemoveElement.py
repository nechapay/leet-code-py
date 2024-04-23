import unittest
from lc_27_RemoveElement import *


class TestRemoveElement(unittest.TestCase):
    def test_case1(self):
        nums = [3, 2, 2, 3]
        expectedNums = [2, 2]
        k = removeElement(nums, 3)
        self.assertEqual(expectedNums.sort(), nums[:k].sort())

    def test_case2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        expectedNums = [0, 1, 4, 0, 3]
        k = removeElement(nums, 2)
        self.assertEqual(expectedNums.sort(), nums[:k].sort())

    def test_case3(self):
        self.assertEqual(removeElement([], 0), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
