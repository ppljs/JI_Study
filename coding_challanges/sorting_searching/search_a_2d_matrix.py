# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/806/

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
"""

def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    smallest_size = len(matrix) if len(matrix) < len(matrix[0]) else len(matrix[0])
    hor_max, ver_max = len(matrix[0]) - 1, len(matrix) - 1
    for i in range(smallest_size):
        hor, found_hor = bin_search(matrix, i, hor_max, target, True)
        ver, found_ver = bin_search(matrix, i, ver_max, target, False)

        if found_hor == True or found_ver == True:
            return True

        if i + 1 > hor and i + 1 > ver:
            return False

        hor_max, ver_max = hor, ver

    return False


def bin_search(matrix, left, right, target, is_horizontal):
    fix = left
    mid_elem = target + 1
    mid = -1
    while left <= right:
        mid = (right + left) // 2
        mid_elem = get_from_matrix(matrix, is_horizontal, fix, mid)
        if mid_elem == target:
            return "anything", True
        elif mid_elem > target:
            right = mid - 1
        else:
            left = mid + 1
    # check later for -1 index
    return mid if mid_elem <= target else mid - 1, False


def get_from_matrix(matrix, is_horizontal, fix, ind):
    return matrix[fix][ind] if is_horizontal else matrix[ind][fix]


# =========================================================================================================
# Why didn't I think of this :`(

def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    max_i, max_j = len(matrix), len(matrix[0])
    i, j = max_i - 1, 0
    while i >= 0 and j < max_j:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            i -= 1
        else:
            j += 1

    return False
