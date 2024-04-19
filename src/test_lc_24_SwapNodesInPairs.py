import unittest
from lc_24_SwapNodesInPairs import *


class TestSwapNodesInPairs(unittest.TestCase):
    def test_case1(self):
        head = arr_to_linked_list([1, 2, 3, 4])
        self.assertEqual(linked_list_to_arr(swapPairs(head)), [2, 1, 4, 3])

    def test_case2(self):
        head = arr_to_linked_list([])
        self.assertEqual(linked_list_to_arr(swapPairs(head)), [])

    def test_case3(self):
        head = arr_to_linked_list([1])
        self.assertEqual(linked_list_to_arr(swapPairs(head)), [1])


if __name__ == '__main__':
    unittest.main(verbosity=2)
