# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/803/

"""
Given a collection of intervals, merge all overlapping intervals.
"""


def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []
    
    intervals = sorted(intervals, key=lambda inter: inter[0])
    merged_intervals = []
    curr_inter = None
    for i in range(len(intervals) - 1):
        if not curr_inter:
            curr_inter = intervals[i]
        
        if should_merge(curr_inter, intervals[i + 1]):
            curr_inter = merge(curr_inter, intervals[i + 1])
        else:
            merged_intervals.append(curr_inter)
            curr_inter = None
    
    merged_intervals.append(get_remaining_interval(curr_inter, intervals))
        
    return merged_intervals


def get_remaining_interval(curr_inter, intervals):
    return curr_inter if curr_inter else intervals[-1]


def should_merge(first, second):
    return first[-1] >= second[0]


def merge(first, second):
    interval_tail = second[-1] if second[-1] > first[-1] else first[-1]
    return [first[0], interval_tail]