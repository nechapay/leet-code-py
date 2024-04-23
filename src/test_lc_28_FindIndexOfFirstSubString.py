import unittest
from lc_28_FindIndexOfFirstSubString import *


class TestFindIndexOfFirstSubString(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(strStr('sadbutsad', "sad"), 0)

    def test_case2(self):
        self.assertEqual(strStr("leetcode", "leeto"), -1)

    def test_case3(self):
        self.assertEqual(strStr('a', "a"), 0)

    def test_case4(self):
        self.assertEqual(strStr("aabaaabaaac", "aabaaac"), 4)

    def test_case5(self):
        self.assertEqual(strStrKMP('sadbutsad', "sad"), 0)

    def test_case6(self):
        self.assertEqual(strStrKMP("leetcode", "leeto"), -1)

    def test_case7(self):
        self.assertEqual(strStrKMP('a', "a"), 0)

    def test_case8(self):
        self.assertEqual(strStrKMP("aabaaabaaac", "aabaaac"), 4)


if __name__ == '__main__':
    unittest.main(verbosity=2)
