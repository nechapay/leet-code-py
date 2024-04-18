import unittest
from lc_8_StringToInteger import *


class TestStringToInteger(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(myAtoi("42"), 42)
        self.assertEqual(myAtoi("    -42"), -42)
        self.assertEqual(myAtoi("4193 with words"), 4193)

    def test_edge_case1(self):
        self.assertEqual(myAtoi("-91283472332"), -2147483648)

    def test_edge_case2(self):
        self.assertEqual(myAtoi("21474836460"), 2147483647)


if __name__ == '__main__':
    unittest.main(verbosity=2)
