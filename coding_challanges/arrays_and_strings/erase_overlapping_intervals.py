# https://leetcode.com/problems/non-overlapping-intervals/submissions/

"""
Given a collection of intervals, find the minimum number of intervals
you need to remove to make the rest of the intervals non-overlapping.
"""


def erase_overlapping_intervals_sorting_by_start(intervals):
    s_intervals = sorted(intervals, key=lambda pair: pair[0])

    to_delete = 0
    # Didn't exceed the time limit (the amortized time complexity will be closer to N*logN due to the break)
    # Will only run at O(n**2) when it will need to delete all but one interval I think
    for curr in range(len(s_intervals) - 2, -1, -1):
        for nexti in range(curr + 1, len(s_intervals)):
            if was_not_removed(s_intervals[nexti]):
                if are_overlapping(s_intervals[curr], s_intervals[nexti]):
                    to_delete += 1
                    s_intervals[curr] = None

                break

    return to_delete

def was_not_removed(interval):
    return interval != None


def are_overlapping(i1, i2):
    return i1[1] > i2[0]

# ==========================================================================================

def erase_overlapping_intervals_sorting_by_end(intervals):
    if not intervals:
        return 0

    s_intervals = sorted(intervals, key=lambda pair: pair[1])
    answer = [s_intervals[0].copy()]
    for i in range(1, len(s_intervals)):
        if answer[i][0] >= answer[-1][1]:
            answer.append(answer[i].copy())
    
    return len(s_intervals) - len(answer)
