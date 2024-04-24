import unittest
from lc_29_DivideTwoIntegers import *


class TestDivideTwoIntegers(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(divide(10, 3), 3)

    def test_case2(self):
        self.assertEqual(divide(7, -3), -2)

    def test_case3(self):
        self.assertEqual(divide(10, 2), 5)

    def test_case4(self):
        self.assertEqual(divide(-1, 1), -1)

    def test_case5(self):
        self.assertEqual(divide(-1, -1), 1)

    def test_case6(self):
        self.assertEqual(divide(-2147483648, -1), 2147483647)

    def test_case6(self):
        self.assertEqual(divide(2147483647, 2), 1073741823)


if __name__ == '__main__':
    unittest.main(verbosity=2)
