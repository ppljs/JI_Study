# https://leetcode.com/problems/diameter-of-binary-tree/

"""
Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
    if not root:
        return 0
    return max(calc_diameter_of_bin_tree(root)) - 1

def calc_diameter_of_bin_tree(node):
    if not node:
        return 0, 0
    
    left, lsum = calc_diameter_of_bin_tree(node.left)
    right, rsum = calc_diameter_of_bin_tree(node.right)    
    curr_sum = left + right
    
    max_side_sum = max(lsum, rsum) 
    returned_sum = max_side_sum if max_side_sum > curr_sum else curr_sum + 1
         
    return max(left, right) + 1, returned_sum