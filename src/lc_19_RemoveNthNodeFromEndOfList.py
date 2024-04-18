# Given the head of a linked list, remove the nth node from the end of the list and return its head.
from utils import *


def removeNthFromEnd(head, n):
    tail = head
    count = 0

    while tail:
        tail = tail.next
        count += 1

    if count == n:
        return head.next
    tail = head

    for _ in range(count - n - 1):
        tail = tail.next

    tail.next = tail.next.next if tail.next else None

    return head


if __name__ == '__main__':
    head = arr_to_linked_list([1])
    print(linked_list_to_arr(removeNthFromEnd(head, 1)))
