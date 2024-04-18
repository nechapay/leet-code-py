import unittest
from lc_13_RomanToInteger import *


class TestRomanToInteger(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(romanToInt('III'), 3)
        self.assertEqual(romanToInt('IV'), 4)
        self.assertEqual(romanToInt('VIII'), 8)
        self.assertEqual(romanToInt('X'), 10)

    def test_edge_case1(self):
        self.assertEqual(romanToInt("LIX"), 59)

    def test_edge_case2(self):
        self.assertEqual(romanToInt("MCMXCIV"), 1994)


if __name__ == '__main__':
    unittest.main(verbosity=2)
