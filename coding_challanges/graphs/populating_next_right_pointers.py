# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/789/
"""
You are given a perfect binary tree where all leaves are on the same level,
and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node,
the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""


from collections import deque


class Node:
    def __init__(self, val=0, left=None, right=None, next_node=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next_node


def connect(root: Node):
    if not root:
        return None

    result = root
    queue = deque([root])
    next_level_queue = deque()
    while True:
        if not queue:
            break
        while queue:
            node = queue.popleft()
            node.next_node = queue[0] if queue else None
            if node.left:
                next_level_queue.extend([node.left, node.right])

        queue, next_level_queue = next_level_queue, queue

    return result
