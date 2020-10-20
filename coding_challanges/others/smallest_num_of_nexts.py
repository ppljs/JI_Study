"""
Given an array in which each index represents the current position of a value in an array
and  the content represents the next position where this value should go to, return the
smallest number os steps for the original array get back in order (elements should be 
unique in array).

Ex:
        arr:  [A   B   C   D]
        next: [4   1   2   3]
        simulation:
            - [A   B   C   D]
            - [B   C   D   A]
            - [C   D   A   B]
            - [D   A   B   C]
            - [A   B   C   D]
            output: 4

ps: the "next" only contains valid indices and is the size of the arr itself.
The "target" indices in the "next" can be arranged in any way but are unique and valid.

Other ex of "next": [1   3   4   2]  
"""

from functools import reduce


def get_smallest_number_of_steps(next_inds):
    next_inds = [ val - 1 for val in next_inds ]
    cycles = { get_cycles_from_index(next_inds, i) for i in range(len(next_inds)) }
    return get_minimum_num_of_cycles(cycles)


def get_cycles_from_index(next_inds, curr_i):
    ori_i = curr_i
    cycles = 1
    while next_inds[curr_i] != ori_i:
        cycles += 1
        curr_i = next_inds[curr_i]
    return cycles


def get_minimum_num_of_cycles(cycles):
    return reduce(lambda curr, prev: lcm(prev, curr), cycles, 1)


def lcm(a, b):
    greater, step, smaller = [a, a, b] if a > b else [b, b, a]
    while True:
        if greater % smaller == 0:
            return greater
        greater += step


if __name__ == '__main__':
    next_inds = [4, 1, 2, 3]
    print(get_smallest_number_of_steps(next_inds))
