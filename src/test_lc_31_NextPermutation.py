import unittest
from lc_31_NextPermutation import *


class TestNextPermutation(unittest.TestCase):
    def test_case1(self):
        nums = [1, 2, 3]
        nextPermutation(nums)
        self.assertEqual(nums, [1, 3, 2])

    def test_case2(self):
        nums = [3, 2, 1]
        nextPermutation(nums)
        self.assertEqual(nums, [1, 2, 3])

    def test_case3(self):
        nums = [1, 1, 5]
        nextPermutation(nums)
        self.assertEqual(nums, [1, 5, 1])


if __name__ == '__main__':
    unittest.main(verbosity=2)
