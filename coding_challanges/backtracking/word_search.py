# https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/797/

"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are
those horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        support_set = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if is_word_in_board(board, word, i, j, support_set):
                    return True
                
        return False


def is_word_in_board(board, word, i, j, already_visited):
    if not word:
        return True
    
    if (i, j) in already_visited:
        return False
    
    if is_out_of_bounds(i, board) or is_out_of_bounds(j, board[0]) or board[i][j] != word[0]:
        return False
    
    already_visited.add((i, j))
    
    for d in directions:
        found = is_word_in_board(board, word[1:], i + d[0], j + d[1], already_visited)
        if found:
            return found
    
    already_visited.remove((i, j))
    return False
    
    
def is_out_of_bounds(index, arr):
    return index >= len(arr) or index < 0 
