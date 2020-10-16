# https://www.youtube.com/watch?v=RVIh0snn4Qc
# In my opinion this problem is very bad, its a lot of not that easy to write code
# that you will probably do not have time to do in an interview.


from collections import deque


def get_max_rectangle_area_in_histogram(histogram):
    increasing_or_equal_inds = deque([0])
    max_area = 0
    for i in range(1, len(histogram)):
        if histogram[i] < histogram[increasing_or_equal_inds[-1]]:
            curr_area = get_maximum_area_until_hight(increasing_or_equal_inds, histogram, histogram[i])
            if curr_area > max_area:
                max_area = curr_area
        
        increasing_or_equal_inds.append(i)
    
    curr_area = get_maximum_area_until_hight(increasing_or_equal_inds, histogram, -1)
    if curr_area > max_area:
        max_area = curr_area

    return max_area


def get_maximum_area_until_hight(increasing_or_equal_inds, histogram, height):
    if not increasing_or_equal_inds:
        return 0

    curr_end_ind = curr_start_ind = increasing_or_equal_inds.pop()
    curr_level = max_area = histogram[curr_end_ind]
    while increasing_or_equal_inds and histogram[increasing_or_equal_inds[-1]] > height:
        if curr_level == histogram[increasing_or_equal_inds[-1]]:
            curr_start_ind = increasing_or_equal_inds.pop()
        else:
            area = (1 + curr_end_ind - curr_start_ind) * histogram[curr_end_ind]
            if area > max_area:
                max_area = area
            
            curr_end_ind = curr_start_ind = increasing_or_equal_inds.pop()
            curr_level = histogram[curr_end_ind]

    area = (1 + curr_end_ind - curr_start_ind) * histogram[curr_end_ind]
    if area > max_area:
        max_area = area

    return max_area


if __name__ == '__main__':
    print(get_max_rectangle_area_in_histogram([1,2,3,4,5,3,3,2]))
