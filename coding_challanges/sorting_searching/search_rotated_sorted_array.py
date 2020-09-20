# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/804/
"""
You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.
"""

# PS: Try OO approach later.......
def search(nums, target):
    if not nums:
        return - 1
    
    real_start = find_real_start(arr=nums)
    
    bin_search_args = None
    if real_start == -1:
        bin_search_args = (nums, 0, len(nums) - 1, target)
    elif is_target_on_right(real_start, target, nums):
        bin_search_args = (nums, real_start, len(nums) - 1, target) 
    else:
        bin_search_args = (nums, 0, real_start - 1, target)
    
    return binary_search(*bin_search_args)


def find_real_start(arr):
    return custom_binary_search(arr, real_start_found_cond, real_start_right_cond, 0, len(arr) - 1, None)


def binary_search(arr, left, right, target):
    return custom_binary_search(arr, normal_found_cond, normal_right_cond, left, right, target)

        
def custom_binary_search(arr, found_cond, right_cond, left, right, target):    
    while left <= right:
        mid = (right + left) // 2
        
        if found_cond(arr, mid, target):
            return mid
        elif right_cond(arr, mid, target, right):
            right = mid - 1
        else:
            left = mid + 1

    return -1       


def is_target_on_right(start_ind, target, arr):
    return arr[start_ind] <= target <= arr[-1]


def real_start_found_cond(arr, mid, target):
    return arr[mid] < arr[mid - 1 if mid != 0 else -1]


def real_start_right_cond(arr, mid, target, right):
    return arr[mid] < arr[right]


def normal_found_cond(arr, mid, target):
    return arr[mid] == target


def normal_right_cond(arr, mid, target, right):
    return arr[mid] > target