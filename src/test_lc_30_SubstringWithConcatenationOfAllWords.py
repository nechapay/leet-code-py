import unittest
from lc_30_SubstringWithConcatenationOfAllWords import *


class TestSubstringWithConcatenationOfAllWords(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(findSubstring(
            "barfoothefoobarman", ["foo", "bar"]), [0, 9])

    def test_case2(self):
        self.assertEqual(findSubstring(
            "barfoofoobarthefoobarman", ["bar", "foo", "the"]), [6, 9, 12])

    def test_case3(self):
        self.assertEqual(findSubstring(
            "wordgoodgoodgoodbestword", ["word", "good", "best", "word"]), [])

    def test_case4(self):
        self.assertEqual(findSubstring(
            "wordgoodgoodgoodbestword", ["word", "good", "best", "good"]), [8])

    def test_case5(self):
        self.assertEqual(findSubstring(
            "lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo", "barr", "wing", "ding", "wing"]), [13])


if __name__ == '__main__':
    unittest.main(verbosity=2)
