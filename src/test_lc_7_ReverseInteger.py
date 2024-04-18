import unittest
from lc_7_ReverseInteger import *


class TestReverseInteger(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(reverse(123), 321)
        self.assertEqual(reverse(-123), -321)
        self.assertEqual(reverse(120), 21)


if __name__ == '__main__':
    unittest.main(verbosity=2)
