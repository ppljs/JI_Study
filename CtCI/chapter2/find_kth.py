import sys
import os
sys.path.insert(0, os.getcwd())
from DataStructures.LinkedList import linkedlist


def find_elem_to_end(k_index, linked_list, result):
    begin_node = linked_list.head
    end_node = linked_list.head
    while k_index > 0:
        end_node = end_node.next
        if end_node is None:
            return None
        k_index -= 1
    
    while end_node.next is not None:
        begin_node = begin_node.next
        end_node = end_node.next

    i = 0
    while begin_node is not None:
        result[i] = begin_node.value
        begin_node = begin_node.next
        i += 1

    return result


def find_elem_to_end_rec(k_index, node, result):
    if node is None:
        return

    find_elem_to_end_rec(k_index, node.next, result)

    if k_index[0] == 0:
        result[0] = node.value
        k_index[0] = -1
        return
    elif k_index[0] < 0:
        return

    result[k_index[0]] = node.value
    k_index[0] -= 1


if __name__ == '__main__':
    linked_list = linkedlist.LinkedList(1)
    linked_list.append([7, -2, 1, -2, 8])
    k = [2]
    result = [0] * (k[0] + 1)
    find_elem_to_end_rec(k, linked_list.head, result)
    print(result)