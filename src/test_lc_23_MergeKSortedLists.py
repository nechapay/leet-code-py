import unittest
from lc_23_MergeKSortedLists import *


class TestMergeKSortedLists(unittest.TestCase):
    def test_case1(self):
        l1 = arr_to_linked_list([1, 4, 5])
        l2 = arr_to_linked_list([1, 3, 4])
        l3 = arr_to_linked_list([2, 6])
        lists = [l1, l2, l3]
        self.assertEqual(linked_list_to_arr(
            mergeKLists(lists)), [1, 1, 2, 3, 4, 4, 5, 6])

    def test_case2(self):
        lists = []
        self.assertEqual(linked_list_to_arr(mergeKLists(lists)), [])

    def test_case3(self):
        l1 = arr_to_linked_list([])
        lists = [l1]
        self.assertEqual(linked_list_to_arr(
            mergeKLists(lists)), [])

    def test_case4(self):
        l1 = arr_to_linked_list([1, 4, 5])
        l2 = arr_to_linked_list([1, 3, 4])
        l3 = arr_to_linked_list([2, 6])
        lists = [l1, l2, l3]
        self.assertEqual(linked_list_to_arr(
            mergeKListsPQ(lists)), [1, 1, 2, 3, 4, 4, 5, 6])

    def test_case5(self):
        lists = []
        self.assertEqual(linked_list_to_arr(mergeKListsPQ(lists)), [])

    def test_case6(self):
        l1 = arr_to_linked_list([])
        lists = [l1]
        self.assertEqual(linked_list_to_arr(
            mergeKListsPQ(lists)), [])


if __name__ == '__main__':
    unittest.main(verbosity=2)
