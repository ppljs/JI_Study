# https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/793/
"""
Given a string containing digits from 2-9 inclusive, return all possible
letter combinations that the number could represent. A mapping of digit to letters
(just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example:
    Input: "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


number_to_letters = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


def letter_combinations(digits: str):
    if not digits:
        return []

    result = []
    curr_combination = []
    combine(digits, result, curr_combination)

    return result


def combine(digits, result, curr_combination, curr_digit_index=0):
    if curr_digit_index >= len(digits):
        result.append(''.join(curr_combination))
        return

    for letter in number_to_letters[digits[curr_digit_index]]:
        curr_combination.append(letter)
        combine(digits, result, curr_combination, curr_digit_index + 1)
        curr_combination.pop()
