import sys
import os
sys.path.insert(0, os.getcwd())
from DataStructures.LinkedList import linkedlist


def sum_lists(node1, node2):
    carry = 0
    result = linkedlist.LinkedNode(None)
    h_result = result

    while True:
        val1 = 0
        val2 = 0
        if node1 is not None:
            val1 = node1.value
            node1 = node1.next
        if node2 is not None:
            val2 = node2.value
            node2 = node2.next

        val = val1 + val2 + carry
        result.value = val % 10
        carry = val // 10

        print

        if node1 is None and node2 is None and carry == 0:
            return h_result
        
        result.next = linkedlist.LinkedNode(None)
        result = result.next


if __name__ == '__main__':
    ll1 = linkedlist.LinkedList(7)
    ll1.append([1, 6])
    ll2 = linkedlist.LinkedList(5)
    ll2.append([9, 2])
    print(ll1)
    print(ll2)
    llr = linkedlist.LinkedList(None)
    llr.head = sum_lists(ll1.head, ll2.head)
    llr.node = llr.head
    print(llr)