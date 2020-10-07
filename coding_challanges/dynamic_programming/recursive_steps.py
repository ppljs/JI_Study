# https://www.youtube.com/watch?v=5o-kdjv7FD0

def get_none_array(size):
    return [None] * size

def num_ways_staircase(n, memory, possible_steps, curr=0):
    if curr == n:
        return 1
    if curr > n:
        return 0
    if memory[curr]:
        return memory[curr]

    counter = 0
    for step in possible_steps:
        counter += num_ways_staircase(n, memory, possible_steps, curr + step)

    memory[curr] = counter
    return counter

qty = 20
print(num_ways_staircase(qty, get_none_array(qty), {5, 6, 7}))
