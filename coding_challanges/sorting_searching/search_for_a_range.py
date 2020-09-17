# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/802/
"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
"""

def search_range(nums, target, use_only_bin_search=True):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (right + left) // 2

        if nums[mid] == target:
            if use_only_bin_search:
                return get_edge_indices_only_binary_search(nums, left, right, mid)
            else:
                return get_edge_indices(nums, mid)
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return [-1, -1]


def get_edge_indices_only_binary_search(nums, left, right, mid):
    return [
        binary_search(nums, nums[mid], left, mid - 1, mid, True),
        binary_search(nums, nums[mid], mid + 1, right, mid, False)
    ]

def binary_search(nums, target, left, right, last_found_ind, going_to_the_left):
    while left <= right:
        mid = (right + left) // 2

        if nums[mid] == target:
            if going_to_the_left:
                return binary_search(nums, target, left, mid - 1, mid, going_to_the_left)
            else:
                return binary_search(nums, target, mid + 1, right, mid, going_to_the_left)
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return last_found_ind


def get_edge_indices(arr, curr_ind):
    return [
        get_edge_index_with_direction(arr, curr_ind, True),
        get_edge_index_with_direction(arr, curr_ind, False)
    ]


def get_edge_index_with_direction(arr, start_ind, go_to_left=True):
    step = -1 if go_to_left else 1
    edge_ind = new_ind = start_ind
    while new_ind > -1 and new_ind < len(arr) and arr[new_ind] == arr[start_ind]:
        edge_ind = new_ind
        new_ind += step
    
    return edge_ind


test_arr = [0,0,0,1,1,2,2,2,4,4,4,4,4,4,5,5,6,7,8]
print([ 
    f"{result[0]} -> {result[1:]}" 
    for result in [
        [target] + search_range(test_arr, target)
        for target in range(len(test_arr))
    ]
])


