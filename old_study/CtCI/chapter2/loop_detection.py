import sys
import os
sys.path.insert(0, os.getcwd())
from DataStructures.LinkedList import linkedlist


def loop_intersection(node):
    head = slow = fast = node

    if fast.next is None or fast.next.next is None:
        return None
    
    fast = fast.next.next
    slow = slow.next

    i = 0
    while slow is not fast:
        slow = slow.next
        while i < 2:
            fast = fast.next
            if fast is None:
                return None
            i += 1
        i = 0
    
    while slow is not head:
        slow = slow.next
        head = head.next
    
    return slow


if __name__ == '__main__':
    ll = linkedlist.LinkedList(1)
    ll.append([2, 3, 4, 5])
    # looping starting at the node with value 3
    ll.head.next.next.next.next.next = ll.head.next.next
    node = loop_intersection(ll.head)
    print(node.value)
