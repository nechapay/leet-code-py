import unittest
from lc_22_GenerateParentheses import *


class TestGenerateParentheses(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(generateParenthesis(
            3), ["((()))", "(()())",  "(())()", "()(())", "()()()"])

    def test_case2(self):
        self.assertEqual(generateParenthesis(1), ["()"])

    def test_case3(self):
        self.assertEqual(generateParenthesis(0), [''])


if __name__ == '__main__':
    unittest.main(verbosity=2)
