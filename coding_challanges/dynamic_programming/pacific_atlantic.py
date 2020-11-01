# https://leetcode.com/problems/pacific-atlantic-water-flow/

"""
SPOILERS BELOW!!!
PS: 
   1. Sorry about this messy code 😣.
   2. This code is not submitting on leet code, I lost my patience trying to know why
   3. There is an easier way of doing this, that is by starting from the pacific or atlantic and every node reachable from the starting position
       can be marked (much less conditionals -> cleaner code)
"""

CANT_REACH = -1
UNKNOWN = 0 # position already visited before, but still not concluded (to not go in circles)
CAN_REACH = 1

A_DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
P_DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def pacificAtlantic(matrix):
    atlantic, pacific = find_pacific_atlantic(matrix)
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if atlantic[i][j] == pacific[i][j] == CAN_REACH:
                result.append([i, j])

    return result
        
def find_pacific_atlantic(matrix):
    a_memory = get_empty_memory(matrix)
    p_memory = get_empty_memory(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            can_reach(matrix, reached_atlantic, A_DIRECTIONS, i, j, matrix[i][j], a_memory)
            can_reach(matrix, reached_pacific, P_DIRECTIONS, i, j, matrix[i][j], p_memory)
            
    return a_memory, p_memory

def can_reach(matrix, reached, directions, i, j, prev, memory):
    if is_out_of_bounds(matrix, i) or is_out_of_bounds(matrix[0], j) or prev < matrix[i][j] or memory[i][j] == UNKNOWN:
        return False
    
    if memory[i][j] == CANT_REACH:
        return False
    
    if memory[i][j] == CAN_REACH or reached(i, j, matrix):
        memory[i][j] = CAN_REACH
        return True
    
    memory[i][j] = UNKNOWN
    for di, dj in directions:
        if can_reach(matrix, reached, directions, i + di, j + dj, matrix[i][j], memory):
            memory[i][j] = CAN_REACH
            return True
    
    memory[i][j] = CANT_REACH
    
    return False


def reached_atlantic(i, j, matrix):
    return i + 1 == len(matrix) or j + 1 == len(matrix[0])

def reached_pacific(i, j, matrix):
    return i == 0 or j == 0

def get_empty_memory(matrix):
    return [ [ None for j in range(len(matrix[0])) ] for i in range(len(matrix)) ]

def is_out_of_bounds(arr, i):
    return i < 0 or i >= len(arr)
