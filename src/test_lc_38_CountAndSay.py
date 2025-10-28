import unittest
from lc_38_CountAndSay import *


class TestCountAndSay(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(countAndSay(4), '1211')

    def test_case2(self):
        self.assertEqual(countAndSay(1), '1')


if __name__ == '__main__':
    unittest.main(verbosity=2)
