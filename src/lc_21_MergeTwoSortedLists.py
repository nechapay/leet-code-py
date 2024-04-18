# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
from utils import *


def mergeTwoLists(list1, list2):
    list1_tail = list1
    list2_tail = list2
    node = head = ListNode()

    while list1_tail and list2_tail:
        if list1_tail.val < list2_tail.val:
            node.next = list1_tail
            list1_tail = list1_tail.next
        else:
            node.next = list2_tail
            list2_tail = list2_tail.next
        node = node.next

    node.next = list1_tail or list2_tail

    return head.next


if __name__ == '__main__':
    list1 = arr_to_linked_list([1, 2, 4])
    list2 = arr_to_linked_list([1, 3, 4])
    print(mergeTwoLists(list1, list2))
