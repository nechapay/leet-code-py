import unittest
from lc_17_LetterCombinationOfPhoneNumber import *


class TestLetterCombinationOfPhoneNumber(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(
            letterCombinations("23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

    def test_case2(self):
        self.assertEqual(letterCombinations(""), [])

    def test_case3(self):
        self.assertEqual(letterCombinations("2"), ["a", "b", "c"])


if __name__ == '__main__':
    unittest.main(verbosity=2)
