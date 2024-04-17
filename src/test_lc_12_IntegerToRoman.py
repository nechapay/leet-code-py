import unittest
from lc_12_IntegerToRoman import *


class TestAddTwoNumbers(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(intToRoman(3), 'III')
        self.assertEqual(intToRoman(4), 'IV')
        self.assertEqual(intToRoman(8), 'VIII')
        self.assertEqual(intToRoman(10), 'X')

    def test_edge_case1(self):
        self.assertEqual(intToRoman(59), "LIX")

    def test_edge_case2(self):
        self.assertEqual(intToRoman(1994), "MCMXCIV")


if __name__ == '__main__':
    unittest.main(verbosity=2)
