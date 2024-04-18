import unittest
from lc_21_MergeTwoSortedLists import *


class TestMergeTwoSortedLists(unittest.TestCase):
    def test_case1(self):
        list1 = arr_to_linked_list([1, 2, 4])
        list2 = arr_to_linked_list([1, 3, 4])
        self.assertEqual(linked_list_to_arr(
            mergeTwoLists(list1, list2)), [1, 1, 2, 3, 4, 4])

    def test_case2(self):
        list1 = arr_to_linked_list([])
        list2 = arr_to_linked_list([])
        self.assertEqual(linked_list_to_arr(
            mergeTwoLists(list1, list2)), [])

    def test_case3(self):
        list1 = arr_to_linked_list([])
        list2 = arr_to_linked_list([0])
        self.assertEqual(linked_list_to_arr(
            mergeTwoLists(list1, list2)), [0])
        

if __name__ == '__main__':
    unittest.main(verbosity=2)
