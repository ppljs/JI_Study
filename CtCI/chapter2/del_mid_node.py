import sys
import os
sys.path.insert(0, os.getcwd())
from DataStructures.LinkedList import linkedlist


def del_mid_node(node_to_del):
    node_to_del.value = node_to_del.next.value
    node_to_del.next = node_to_del.next.next


if __name__ == '__main__':
    linked_list = linkedlist.LinkedList(1)
    linked_list.append([7, -2, 1, -2])
    print(linked_list)
    # The node with value 7 (the second node) is deleted
    del_mid_node(linked_list.head.next)
    print(linked_list)
