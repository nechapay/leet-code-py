
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_matrix(mtx, s=''):
    print(s)
    for i in range(len(mtx)):
        print('|', end=" ")
        for j in range(len(mtx[i])):
            elem = 1 if mtx[i][j] else 0
            print(elem, end=" ")
        print("|")
    return ''


def arr_to_linked_list(arr):
    h = ListNode()
    t = h
    for i in arr:
        t.next = ListNode(i)
        t = t.next
    return h.next


def linked_list_to_arr(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr
