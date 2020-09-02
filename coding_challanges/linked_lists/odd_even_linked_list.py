#https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/784/
"""
Given a singly linked list, group all odd nodes together followed by the even nodes.
 Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity
 and O(nodes) time complexity.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def odd_even_linked_list(root_node):
    if not root_node:
        return None

    curr_node = root_node
    tail_node, list_size = get_tail_node_and_size(root_node)
    if list_size < 3:
        return root_node

    number_of_iterations = list_size // 2

    for i in range(number_of_iterations):
        tail_node = put_next_node_on_back_and_get_last(curr_node, tail_node)
        curr_node = curr_node.next

    return root_node


def put_next_node_on_back_and_get_last(curr_node, tail_node):
    moved_node = curr_node.next
    tail_node.next = moved_node
    curr_node.next = moved_node.next
    moved_node.next = None

    return moved_node


def get_tail_node_and_size(root_node):
    size = 1
    while root_node.next:
        size += 1
        root_node = root_node.next
    return root_node, size


def print_linked_list(root_node):
    while root_node:
        print(f" {root_node.val} ->", end='')
        root_node = root_node.next


def array_to_linked_list(arr):
    linked_list = ListNode()
    root_node = linked_list
    for ind, elem in enumerate(arr):
        linked_list.val = elem
        if ind < len(arr) - 1:
            linked_list.next = ListNode()
            linked_list = linked_list.next

    return root_node


if __name__ == '__main__':
    test_list = array_to_linked_list([1,2,3,4,5,6,7,8,9,10,11,12])
    print_linked_list(odd_even_linked_list(test_list))

# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
# 1 -> 3 -> 2 -> 4 -> 5 -> 6 -> 7
# 1 -> 3 -> 5 -> 2 -> 4 -> 6 -> 7
#
# 1 -> 2 -> 3 -> 4 -> 5 -> 6
# 1 -> 3 -> 4 -> 5 -> 6 -> 2
# 1 -> 3 -> 5 -> 6 -> 2 -> 4
#