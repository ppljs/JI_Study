
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

"""
Given a sorted array nums, remove the duplicates in-place such that each element appears
only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the
input array in-place with O(1) extra memory.
"""

def removeDuplicates(nums):
    if not nums:
        return 0
    repetitions = 0
    curr_num = nums[0]
    free_pos = 1
    for i in range(1, len(nums)):
        if nums[i] == curr_num:
            repetitions += 1
        else:
            curr_num = nums[i]
            nums[free_pos] = nums[i]
            free_pos += 1
            
    
    return len(nums) - repetitions