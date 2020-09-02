# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""
Given a binary search tree, write a function kthSmallest to find the kth
smallest element in it.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root, k):
    return find_kth_smallest(root, k, [0])


def find_kth_smallest(node, k, counter):
    if not node:
        return None

    result = find_kth_smallest(node.left, k, counter)
    if result is None:
        counter[0] += 1
        if counter[0] == k:
            return node.val
    else:
        return result

    return find_kth_smallest(node.right, k, counter)