import unittest
from lc_25_ReverseNodesInKGroup import *


class TestReverseNodesInKGroup(unittest.TestCase):
    def test_case1(self):
        head = arr_to_linked_list([1, 2, 3, 4, 5])
        self.assertEqual(linked_list_to_arr(
            reverseKGroup(head, 2)), [2, 1, 4, 3, 5])

    def test_case2(self):
        head = arr_to_linked_list([1, 2, 3, 4, 5])
        self.assertEqual(linked_list_to_arr(
            reverseKGroup(head, 3)), [3, 2, 1, 4, 5])

    def test_case3(self):
        head = arr_to_linked_list([1, 2])
        self.assertEqual(linked_list_to_arr(reverseKGroup(head, 3)), [1, 2])


if __name__ == '__main__':
    unittest.main(verbosity=2)
