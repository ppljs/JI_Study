# https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/796/
"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
"""

def subsets(nums):
    if not nums:
        return [[]]

    nums = set(nums)
    result = []
    curr_sub = []
    for size in range(len(nums) + 1):
        generate_subsets(nums, result, curr_sub, size)

    return result


def generate_subsets(nums, result, curr_sub, size_limit):
    if len(curr_sub) >= size_limit:
        result.append(curr_sub.copy())
        return

    if not nums:
        return

    used_set = set()
    for num in nums:
        curr_sub.append(num)
        used_set.add(num)
        generate_subsets(nums - used_set, result, curr_sub, size_limit)
        curr_sub.pop()
