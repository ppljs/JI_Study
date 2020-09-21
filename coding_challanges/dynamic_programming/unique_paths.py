# https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/808/

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot
is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""


from math import factorial


def uniquePaths(m, n):
    # Dynamic Programming solution
    memory = [[0 for j in range(n)] for i in range(m)]
    memory[-1][-1] = 1
    get_unique_paths(memory, 0, 0)
    return memory[0][0]

    # Math solution
    # return permutation_with_repetition(m - 1, n - 1)


def permutation_with_repetition(m, n):
    return factorial(m + n) // (factorial(m) * factorial(n))


def get_unique_paths(memory, curr_m, curr_n):
    if curr_m >= len(memory) or curr_n >= len(memory[0]):
        return 0

    if memory[curr_m][curr_n] > 0:
        return memory[curr_m][curr_n]

    memory[curr_m][curr_n] += get_unique_paths(memory, curr_m, curr_n + 1)
    memory[curr_m][curr_n] += get_unique_paths(memory, curr_m + 1, curr_n)

    return memory[curr_m][curr_n]
