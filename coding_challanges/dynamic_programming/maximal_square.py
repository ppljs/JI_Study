# https://leetcode.com/problems/maximal-square/submissions/


def maximalSquare(matrix):
    max_size = 0

    if not matrix or not isinstance(matrix[0], list):
        return 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '1':
                curr = get_min_value_of_previous_places(i, j, matrix) + 1
                matrix[i][j] = curr
                if curr > max_size:
                    max_size = curr
            else:
                matrix[i][j] = 0

    return max_size ** 2

def get_min_value_of_previous_places(i, j, memory):
    if is_out_of_bounds(i - 1, memory) or is_out_of_bounds(j - 1, memory[0]):
        return 0
    
    return min(memory[i-1][j], memory[i][j-1], memory[i-1][j-1])

def is_out_of_bounds(index, arr):
    return index < 0 or index >= len(arr)
