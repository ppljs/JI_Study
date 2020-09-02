# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/786/
"""
Given a binary tree, return the inorder traversal of its nodes' values.
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


def in_order_traversal(root):
    return get_tree_as_arr_in_order_it(root)


def get_tree_as_arr_in_order(root, result):
    if not root:
        return
    get_tree_as_arr_in_order(root.left, result)
    result.append(root.val)
    get_tree_as_arr_in_order(root.right, result)


def get_tree_as_arr_in_order_it(node):
    result = []
    exec_stack = deque()
    while True:
        if node.left:
            exec_stack.append(node)
            node = node.left
        elif node.right:
            result.append(node.val)
            node = node.right
        else:
            result.append(node.val)
            if not exec_stack:
                break

            while True:
                if not exec_stack:
                    return result
                node = exec_stack.pop()
                result.append(node.val)
                if node.right:
                    node = node.right
                    break

    return result


def print_tree_in_order(root):
    if not root:
        return
    print_tree_in_order(root.left)
    print(root.val)
    print_tree_in_order(root.right)


head = TreeNode(1, None, TreeNode(3, TreeNode(2), None))
w(get_tree_as_arr_in_order_it(head))
