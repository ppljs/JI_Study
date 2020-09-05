# https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/794/
"""
Given n pairs of parentheses, write a function to generate all
combinations of well-formed parentheses.
"""


def generate_parenthesis(n):
    result = []
    generate(n, 0, 0, "", result)

    return result


def generate(n, open_p, close_p, new_comb, result):
    if open_p > n or close_p > open_p:
        return
    if (open_p + close_p) // 2 == n:
        result.append(new_comb)
        return

    generate(n, open_p + 1, close_p, new_comb + "(", result)
    generate(n, open_p, close_p + 1, new_comb + ")", result)
