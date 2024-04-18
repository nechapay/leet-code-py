import unittest
from lc_14_LongestCommonPrefix import *


class TestLongestCommonPrefix(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(longestCommonPrefix(
            ["flower", "flow", "flight"]), "fl")

    def test_edge_case1(self):
        self.assertEqual(longestCommonPrefix(["dog", "racecar", "car"]), "")

    def test_edge_case2(self):
        self.assertEqual(longestCommonPrefix(["aaa", "aab", "abc"]), "a")


if __name__ == '__main__':
    unittest.main(verbosity=2)
