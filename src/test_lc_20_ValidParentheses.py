import unittest
from lc_20_ValidParentheses import *


class TestValidParentheses(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(isValid("()"), True)

    def test_case2(self):
        self.assertEqual(isValid("()[]{}"), True)

    def test_case3(self):
        self.assertEqual(isValid("(]"), False)

    def test_case4(self):
        self.assertEqual(isValid("(())]"), False)

    def test_case5(self):
        self.assertEqual(isValid("{[]}"), True)

    def test_case6(self):
        self.assertEqual(isValid("["), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
