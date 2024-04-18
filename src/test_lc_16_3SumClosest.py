import unittest
from lc_16_3SumClosest import *


class Test3SumClosest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(
            threeSumClosest([-1, 2, 1, -4], 1), 2)

    def test_case2(self):
        self.assertEqual(threeSumClosest([0, 0, 0], 1), 0)

    def test_case3(self):
        self.assertEqual(threeSumClosest([0, 1, 2], 0), 3)

    def test_case4(self):
        self.assertEqual(threeSumClosest([1, 1, -1], 2), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
