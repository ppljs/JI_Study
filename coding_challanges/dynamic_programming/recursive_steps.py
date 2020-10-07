# https://www.youtube.com/watch?v=5o-kdjv7FD0

from functools import reduce

def get_none_array(size):
    return [None] * size

def num_ways_staircase(n, memory, possible_steps, curr=0):
    if curr == n:
        return 1
    if curr > n:
        return 0
    if memory[curr]:
        return memory[curr]

    possibilities = reduce(
        lambda prev, step: prev + num_ways_staircase(n, memory, possible_steps, curr + step),
        possible_steps,
        0
    )

    memory[curr] = possibilities
    return possibilities

qty = 20
print(num_ways_staircase(qty, get_none_array(qty), {1, 2}))
