# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
from utils import *
import heapq


def mergeKLists(lists):
    head = out = ListNode()

    if not lists:
        return None

    if len(lists) == 1:
        return lists[0]

    tail1 = lists[0]
    for i in range(1, len(lists)):
        tail2 = lists[i]
        while tail1 and tail2:
            if tail1.val < tail2.val:
                out.next = tail1
                tail1 = tail1.next
            else:
                out.next = tail2
                tail2 = tail2.next
            out = out.next
        out.next = tail1 or tail2
        out = head
        tail1 = out.next

    return head.next


def mergeKListsPQ(lists):
    head = ListNode()
    curr = head
    heap = []

    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i))
            lists[i] = lists[i].next

    while heap:
        val, i = heapq.heappop(heap)
        curr.next = ListNode(val)
        curr = curr.next
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i))
            lists[i] = lists[i].next

    return head.next


if __name__ == '__main__':
    l1 = arr_to_linked_list([1, 4, 5])
    l2 = arr_to_linked_list([1, 3, 4])
    l3 = arr_to_linked_list([2, 6])
    lists = [l1, l2, l3]
    # print(linked_list_to_arr(mergeKLists(lists)))
    print(linked_list_to_arr(mergeKListsPQ(lists)))
