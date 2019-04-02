import sys
import os
sys.path.insert(0, os.getcwd())
from DataStructures.LinkedList import linkedlist


# More stable
def partition(head, value):
    h_less = less = h_more = more = None
    curr = head
    while curr is not None:
        if curr.value < value:
            if less is None:
                less = h_less = linkedlist.LinkedNode(curr.value)
            else:
                less.next = linkedlist.LinkedNode(curr.value)
                less = less.next
        else:
            if more is None:
                more = h_more = linkedlist.LinkedNode(curr.value)
            else:
                more.next = linkedlist.LinkedNode(curr.value)
                more = more.next
        curr = curr.next

    if h_less is None:
        return
    head.value = h_less.value
    head.next = h_less.next
    less.next = h_more


# Less stable
def partition2(head, value):
    new_head = head
    new_tail = head
    curr = head
    while curr is not None:
        curr_next = curr.next
        if curr.value < value:
            curr.next = new_head
            new_head = curr
        else:
            new_tail.next = curr
            new_tail = curr
        curr = curr_next
    new_tail.next = None

    return new_head


if __name__ == '__main__':
    linked_list = linkedlist.LinkedList(1)
    linked_list.append([7, -2, 1, -2])
    print(linked_list)
    linked_list.head = partition2(linked_list.head, 1)
    print(linked_list)
    print(linked_list.head.value)