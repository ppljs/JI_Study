# https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/785/
"""
Write a program to find the node at which the intersection of
 two singly linked lists begins.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_intersection_node(first, second):
    biggest, smallest, size_diff = get_biggest_and_smallest_list_heads_and_size_diff(first, second)
    biggest_adv = get_advanced_biggest_head(biggest, size_diff)

    return find_intersection_node(biggest_adv, smallest)


def find_intersection_node(biggest_adv_head, smallest_head):
    while biggest_adv_head:
        if biggest_adv_head is smallest_head:
            return biggest_adv_head
        biggest_adv_head, smallest_head = biggest_adv_head.next, smallest_head.next

    return None


def get_biggest_and_smallest_list_heads_and_size_diff(first, second):
    first_size = get_list_size(first)
    second_size = get_list_size(second)

    return [first, second, first_size - second_size] if first_size > second_size\
        else [second, first, second_size - first_size]


def get_advanced_biggest_head(biggest_head, size_diff):
    for i in range(size_diff):
        biggest_head = biggest_head.next

    return biggest_head


def get_list_size(head):
    size = 0
    while head:
        size += 1
        head = head.next

    return size