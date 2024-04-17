import unittest
from lc_6_ZigzagConversion import *


class TestTwoSum(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
        self.assertEqual(convert("A", 1), "A")


if __name__ == '__main__':
    unittest.main(verbosity=2)
