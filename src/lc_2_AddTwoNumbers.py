# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

from utils import *

def addTwoNumbers(l1, l2):
    head = ListNode()
    tail = head
    c = 0
    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        sum = c + x + y

        c = sum // 10
        tail.next = ListNode(sum % 10)
        tail = tail.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    if c > 0:
        tail.next = ListNode(c)

    return head.next




l1 = arr_to_linked_list([2, 4, 3])
l2 = arr_to_linked_list([5, 6, 4])
print(linked_list_to_arr(addTwoNumbers(l1, l2)))
