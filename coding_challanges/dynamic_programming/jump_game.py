# https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/807/

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
"""


def can_jump(nums):    
    left_good = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] + i >= left_good:
            left_good = i
    
    return left_good == 0