# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.

from utils import *


def reverseKGroup(head, k):
    dummy = prevEnd = ListNode()
    dummy.next = head
    prevEnd.next = head
    curr = currEnd = head
    prev = None
    count = 1

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

        if count % k == 0:
            prevEnd.next = prev
            prevEnd = currEnd
            currEnd = curr
            prev = None
        count += 1

    curr = prev
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    prevEnd.next = prev

    return dummy.next


if __name__ == '__main__':
    head = arr_to_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(linked_list_to_arr(reverseKGroup(head, 4)))
