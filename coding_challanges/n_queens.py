from collections import deque
from time import time


def timeit(func):
    def measure_exec_time(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f"Time spent of function: {(time() - start) * 1000}[ms]")
        return result

    return measure_exec_time


def is_valid_queen_pos(i, j, queens_pos):
    for qi, qj in queens_pos:
        ri, rj = abs(qi - i), abs(qj - j)
        if min(ri, rj) == 0 or ri == rj:
            return False
    
    return True

@timeit
def get_n_queens_position_slow(n):
    queens_pos = deque()
    def put_n_queens(i=0):
        for j in range(n):
            if is_valid_queen_pos(i, j, queens_pos):
                queens_pos.append((i, j))
                if len(queens_pos) == n:
                    return True

                result = put_n_queens(i + 1)
                if result:
                    return True
                else:
                    queens_pos.pop()

    put_n_queens()
    return queens_pos


@timeit
def get_n_queens_position(n):
    queens_pos = deque()
    available_cols = { i for i in range(n) }
    def put_n_queens(i=0):
        for j in available_cols:
            if is_valid_queen_pos(i, j, queens_pos):
                queens_pos.append((i, j))
                if len(queens_pos) == n:
                    return True
                available_cols.remove(j)
                result = put_n_queens(i + 1)
                if result:
                    return True
                else:
                    available_cols.add(j)
                    queens_pos.pop()

    put_n_queens()
    return queens_pos


if __name__ == '__main__':
    get_n_queens_position(20)
    get_n_queens_position_slow(20)