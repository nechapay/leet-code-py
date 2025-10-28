import unittest
from lc_39_CombinationSum import *


class TestCombinationSum(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(combinationSum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])

    def test_case2(self):
        self.assertEqual(combinationSum([2, 3, 5], 8), [
                         [2, 2, 2, 2], [2, 3, 3], [3, 5]])

    def test_case3(self):
        self.assertEqual(combinationSumDP([2, 3, 6, 7], 7), [[2, 2, 3], [7]])

    def test_case4(self):
        self.assertEqual(combinationSumDP([2, 3, 5], 8), [
                         [2, 2, 2, 2], [2, 3, 3], [3, 5]])


if __name__ == '__main__':
    unittest.main(verbosity=2)
