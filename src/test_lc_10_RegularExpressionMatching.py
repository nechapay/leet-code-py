import unittest
from lc_10_RegularExpressionMatching import *


class TestRegularExpressionMatching(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(isMatch("aa", "a"), False)

    def test_edge_case1(self):
        self.assertEqual(isMatch("aa", "a*"), True)

    def test_edge_case2(self):
        self.assertEqual(isMatch("ab", ""), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
