# https://leetcode.com/problems/rotting-oranges/

from collections import deque


DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def orangesRotting(grid):
    if not grid or not grid[0]:
        return -1

    total_fresh = count_fresh(grid)
    rotten_queue = deque(get_rotten_positions(grid))
    next_queue = deque()
    elapsed_time = 0

    while rotten_queue:
        curr_rotten = rotten_queue.popleft()
        new_rottens = spread(grid, curr_rotten[0], curr_rotten[1])
        next_queue.extend(new_rottens)
        total_fresh -= len(new_rottens)
        if total_fresh == 0:
            return elapsed_time + 1 if new_rottens else elapsed_time

        if not rotten_queue:
            elapsed_time += 1
            rotten_queue, next_queue = next_queue, rotten_queue

    return 0 if total_fresh == 0 else -1
            

def spread(matrix, i, j):
    new_rottens = []
    for di, dj in DIRECTIONS:
        newi, newj = i + di, j + dj
        if is_fresh(matrix, newi, newj):
            matrix[newi][newj] = 2
            new_rottens.append((newi, newj))
    
    return new_rottens
        
def get_rotten_positions(matrix):
    return [ (i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == 2 ]

def count_fresh(matrix):
    fresh = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                fresh += 1

    return fresh


def is_fresh(matrix, i, j):
    return is_inbounds(i, matrix) and is_inbounds(j, matrix[0]) and matrix[i][j] == 1


def is_inbounds(k, arr):
    return k >= 0 and k < len(arr)
