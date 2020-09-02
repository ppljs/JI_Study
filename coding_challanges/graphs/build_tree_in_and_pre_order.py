# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/788/

"""
Given preorder and inorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    preorder = deque(preorder)
    return build_tree_rec(preorder, inorder)


def build_tree_rec(preorder, inorder):
    if inorder:
        root = TreeNode(preorder.popleft())
        root_ind = inorder.index(root.val)
        root.left = build_tree_rec(preorder, inorder[:root_ind])
        root.right = build_tree_rec(preorder, inorder[root_ind + 1:])
        return root
    else:
        return None
