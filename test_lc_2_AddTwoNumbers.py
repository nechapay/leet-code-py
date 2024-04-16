import unittest
from lc_2_AddTwoNumbers import *


class TestAddTwoNumbers(unittest.TestCase):
    def test_equal(self):
        l1 = arr_to_linked_list([2, 4, 3])
        l2 = arr_to_linked_list([5, 6, 4])
        self.assertEqual(linked_list_to_arr(addTwoNumbers(l1, l2)), [7, 0, 8])
        l1 = arr_to_linked_list([0])
        l2 = arr_to_linked_list([0])
        self.assertEqual(linked_list_to_arr(addTwoNumbers(l1, l2)), [0])
        l1 = arr_to_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = arr_to_linked_list([9, 9, 9, 9])
        self.assertEqual(linked_list_to_arr(
            addTwoNumbers(l1, l2)), [8, 9, 9, 9, 0, 0, 0, 1])


if __name__ == '__main__':
    unittest.main(verbosity=2)
