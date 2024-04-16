import unittest
from lc_4_MedianOfTwoSortedArrays import *


class TestMedianOfTwoSortedArrays(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(findMedianSortedArrays([1, 3], [2]), 2.00000)
        self.assertEqual(findMedianSortedArrays([1, 2], [3, 4]), 2.50000)


if __name__ == '__main__':
    unittest.main(verbosity=2)
