import unittest
from lc_1_TwoSum import twoSum


class TestTwoSum(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(twoSum([2, 7, 11, 15], 13), [0, 2])
        self.assertEqual(twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(twoSum([2, 7, 11, 15], 1), [])


if __name__ == '__main__':
    unittest.main(verbosity=2)
