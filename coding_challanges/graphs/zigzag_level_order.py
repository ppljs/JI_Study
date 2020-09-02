# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/787/
"""
Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).
"""


from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def get_items_in_zigzag(root):
    if not root:
        return []

    queue = deque()
    queue.append(root)
    next_queue = deque()
    result = [[root.val]]
    curr_row = []

    start_left = False

    while True:

        fill_next_queue(queue, next_queue, start_left, curr_row)
        if next_queue:
            result.append(curr_row)
            curr_row = []
            queue, next_queue = next_queue, queue
            start_left = not start_left
        else:
            break

    return result


def fill_next_queue(queue, next_queue, start_left, curr_row):
    while queue:
        curr_node = queue.pop()
        append_nodes(next_queue, curr_node, start_left, curr_row)


def append_nodes(queue, curr_node, start_left, curr_row):
    first, second = [curr_node.left, curr_node.right] if start_left else [curr_node.right, curr_node.left]
    append_node(queue, first, curr_row)
    append_node(queue, second, curr_row)


def append_node(queue, node, curr_row):
    if node:
        queue.append(node)
        curr_row.append(node.val)