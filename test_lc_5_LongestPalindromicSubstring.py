import unittest
from lc_5_LongestPalindromicSubstring import *


class TestLongestPalindromicSubstring(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(longestPalindrome("babad"), "bab")
        self.assertEqual(longestPalindrome("cbbd"), "bb")
        self.assertEqual(longestPalindrome(""), "")


if __name__ == '__main__':
    unittest.main(verbosity=2)
