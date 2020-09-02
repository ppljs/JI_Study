# https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/783/
"""
You are given two non-empty linked lists representing two
non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two
numbers and return it as a linked list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __len__(self):
        size = 0
        current_node = self
        while current_node:
            size += 1
            current_node = self.next

        return size


def add_two_numbers(first, second):
    biggest, smallest = [first, second] if len(first) > len(second) else [second, first]

    carry = 0
    result_head = ListNode()
    current_node = result_head
    while True:
        current_node.val, carry = sum_two_digits(smallest.val, biggest.val, carry)
        smallest, biggest = smallest.next, biggest.next
        if smallest:
            current_node.next = ListNode()
        else:
            break

    while biggest and carry:
        value, carry = sum_two_digits(0, biggest.val, carry)
        current_node.next = ListNode(value, None)
        current_node = current_node.next
        biggest = biggest.next

    if carry == 1:
        current_node.next = ListNode(1, None)

    return result_head


def sum_two_digits(first, second, carry):
    result = first + second + carry
    result, carry = result % 10, result // 10

    return result, carry
