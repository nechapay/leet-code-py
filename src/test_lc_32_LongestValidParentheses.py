import unittest
from lc_32_LongestValidParentheses import *


class TestNextPermutation(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(longestValidParentheses("(()"), 2)

    def test_case2(self):
        self.assertEqual(longestValidParentheses(")()())"), 4)

    def test_case3(self):
        self.assertEqual(longestValidParentheses(""), 0)

    def test_case4(self):
        self.assertEqual(longestValidParentheses("()(()"), 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
