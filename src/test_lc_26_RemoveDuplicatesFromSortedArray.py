import unittest
from lc_26_RemoveDuplicatesFromSortedArray import *


class TestRemoveDuplicatesFromSortedArray(unittest.TestCase):
    def test_case1(self):
        nums = [1, 1, 2]
        expectedNums = [1, 2]
        k = removeDuplicates(nums)
        self.assertEqual(expectedNums, nums[:k])

    def test_case2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expectedNums = [0, 1, 2, 3, 4]
        k = removeDuplicates(nums)
        self.assertEqual(expectedNums, nums[:k])

    def test_case3(self):
        nums = [1, 1, 1]
        expectedNums = [1]
        k = removeDuplicates(nums)
        self.assertEqual(expectedNums, nums[:k])

    def test_case4(self):
        self.assertEqual(removeDuplicates([]), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
