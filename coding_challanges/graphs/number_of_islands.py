# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/792/
"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
"""


# Possible follow up question could be to make this function generic in order for it to identify
# blobs containing a group of specified characters instead of only counting blobs of "1".
# In this case you might receive a list that you can transform into a Set and then you can check if the
# current character belongs to that Set.

def num_islands(grid):
    if not grid:
        return 0

    island_number = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                turn_adjacent_ones_to_zeros(grid, i, j)
                island_number += 1

    return island_number


def turn_adjacent_ones_to_zeros(grid, i, j):
    if is_index_out_of_bounds(grid, i) or is_index_out_of_bounds(grid[0], j) or grid[i][j] == "0":
        return

    grid[i][j] = "0"
    turn_adjacent_ones_to_zeros(grid, i, j + 1)
    turn_adjacent_ones_to_zeros(grid, i + 1, j)
    turn_adjacent_ones_to_zeros(grid, i, j - 1)
    turn_adjacent_ones_to_zeros(grid, i - 1, j)


def is_index_out_of_bounds(arr, index):
    return index >= len(arr) or index < 0
