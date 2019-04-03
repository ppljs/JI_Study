import sys
import os
sys.path.insert(0, os.getcwd())
from DataStructures.LinkedList import linkedlist


def get_length(node):
    length = 0
    while node is not None:
        node = node.next
        length += 1

    return length


def get_intersection(node1, node2):
    length1 = get_length(node1)
    length2 = get_length(node2)

    to_advance = abs(length1 - length2)
    if length1 < length2:
        tmp = node1
        node1 = node2
        node2 = tmp
    
    while to_advance > 0:
        node1 = node1.next
        to_advance -= 1

    while node1 is not None:
        if node1 is node2:
            return node1
        node1 = node1.next
        node2 = node2.next

    return None


if __name__ == '__main__':
    ll1 = linkedlist.LinkedList(1)
    ll1.append([2, 3, 4, 5])
    ll2 = linkedlist.LinkedList(6)
    ll2.append([7, 8])
    ll2.head.next.next.next = ll1.head.next.next
    print(ll1)
    print(ll2)
    node = get_intersection(ll2.head, ll1.head)
    if node is None:
        print('The lists do not have an intersection...')
    else:
        print(node.value)