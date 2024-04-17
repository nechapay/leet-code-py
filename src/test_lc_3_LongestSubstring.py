import unittest
from lc_3_LongestSubstring import *


class TestLongestSubstring(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(lengthOfLongestSubstring("pwwkew"), 3)


if __name__ == '__main__':
    unittest.main(verbosity=2)
