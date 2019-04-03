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


def sum_i_lists(result, node1, node2, counter=-1):
    if node1 is None:
        return 0
    
    counter += 1
    if counter != 0:
        result.next = linkedlist.LinkedNode(None)
        result = result.next
    
    result.value = node1.value + node2.value + sum_i_lists(result, node1.next, node2.next, counter)
    carry = result.value // 10
    result.value %= 10

    if counter != 0:
        return carry
    else:
        if carry > 0:
            head = linkedlist.LinkedNode(carry)
            head.next = result
            return head
        else:
            return result


def to_same_size(node1, node2):
    counter1 = 0
    counter2 = 0
    h_node1 = node1
    h_node2 = node2

    while node1 is not None:
        counter1 += 1
        node1 = node1.next
    
    while node2 is not None:
        counter2 += 1
        node2 = node2.next

    counter = abs(counter1 - counter2)
    to_expand = h_node1 if counter1 < counter2 else h_node2

    for i in range(counter):
        tmp_node = linkedlist.LinkedNode(0)
        tmp_node.next = to_expand
        to_expand = tmp_node

    if counter1 < counter2:
        return to_expand, h_node2
    else:
        return h_node1, to_expand


def sum_inverted_lists(node1, node2):
    node1, node2 = to_same_size(node1, node2)
    result = linkedlist.LinkedList(None)
    result.head = sum_i_lists(result.head, node1, node2)
    return result


if __name__ == '__main__':
    ll1 = linkedlist.LinkedList(7)
    ll1.append([1, 6, 0])
    ll2 = linkedlist.LinkedList(5)
    ll2.append([9, 2])
    print(ll1)
    print(ll2)
    result = sum_inverted_lists(ll1.head, ll2.head)
    print(result)