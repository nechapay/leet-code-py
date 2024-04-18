import unittest
from lc_19_RemoveNthNodeFromEndOfList import *


class TestRemoveNthNodeFromEndOfList(unittest.TestCase):
    def test_case1(self):
        head = arr_to_linked_list([1, 2, 3, 4, 5])
        self.assertEqual(
            linked_list_to_arr(removeNthFromEnd(head, 2)), [1, 2, 3, 5])

    def test_case2(self):
        head = arr_to_linked_list([1])
        self.assertEqual(
            linked_list_to_arr(removeNthFromEnd(head, 1)), [])

    def test_case3(self):
        head = arr_to_linked_list([1, 2])
        self.assertEqual(
            linked_list_to_arr(removeNthFromEnd(head, 1)), [1])

    def test_case4(self):
        head = arr_to_linked_list([1, 2, 3, 4, 5])
        self.assertEqual(
            linked_list_to_arr(removeNthFromEnd(head, 2)), [1, 2, 3, 5])


if __name__ == '__main__':
    unittest.main(verbosity=2)
