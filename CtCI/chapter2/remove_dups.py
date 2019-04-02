import sys
import os
sys.path.insert(0, os.getcwd())
from DataStructures.LinkedList import linkedlist

# If I would not be able to have a support data structure as I have here (python's 'set'),
# to remove the duplicates from this linked list in less than O(N**2) I would need a doubly linked
# list with a quicksort algorithm made for linked lists, because quicksort does not use support
# arrays to sort and it has a time complexity of O(N*log(N)). 
# After sorting, to eliminate duplicates would be easy, since the duplicates would be side by side.
# So te big O of the whole algorithm would be the big O from quicksort: O(N * log(N)).

def remove_dups(linked_list):
    if linked_list is None or linked_list.head.next is None:
        return

    checker = set()
    checker.add(linked_list.head.value)
    curr_node = linked_list.head
    while curr_node.next is not None:
        if curr_node.next.value in checker:
            curr_node.next = curr_node.next.next
        else:
            checker.add(curr_node.next.value)
            curr_node = curr_node.next


# This is the possible solution with the singly linked list, where the Otime(N**2) but the Ospace(1)
def remove_dups_brute(linked_list):
    if linked_list is None or linked_list.head.next is None:
        return

    fixed_node = linked_list.head

    while fixed_node is not None and fixed_node.next is not None:
        moving_node = fixed_node
        while moving_node.next is not None:
            if fixed_node.value == moving_node.next.value:
                moving_node.next = moving_node.next.next
            else:
                moving_node = moving_node.next
        fixed_node = fixed_node.next


if __name__ == '__main__':
    linked_list = linkedlist.LinkedList(1)
    linked_list.append([7, -2, 1, -2])
    print(linked_list)
    remove_dups_brute(linked_list)
    print(linked_list)