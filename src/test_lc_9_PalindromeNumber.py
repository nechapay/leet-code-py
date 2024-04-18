import unittest
from lc_9_PalindromeNumber import *


class TestPalindromeNumber(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(isPalindrome(121), True)
        self.assertEqual(isPalindrome(-121), False)
        self.assertEqual(isPalindrome(123), False)

    def test_edge_case1(self):
        self.assertEqual(isPalindrome(10), False)

    def test_edge_case2(self):
        self.assertEqual(isPalindrome(0), True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
