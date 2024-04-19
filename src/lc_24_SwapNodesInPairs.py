# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)
from utils import *


def swapPairs(head):
    current = head
    prev = res = None

    while current:
        if not current.next:
            break

        temp = current.next.next
        node1 = current
        node2 = current.next

        node1.next = temp
        node2.next = node1

        if prev:
            prev.next = node2

        if not prev:
            res = node2

        prev = node1

        current = temp

    if res:
        res.next = head
    else:
        res = head

    return res


if __name__ == '__main__':
    head = arr_to_linked_list([1, 2, 3, 4])
    print(linked_list_to_arr(swapPairs(head)))
