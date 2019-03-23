def get_pivot_index(array, start_index, end_index):
    mid_in = (end_index - start_index) // 2
    left = array[start_index]
    right = array[end_index]
    mid = array[mid_in]

    if (left < mid and mid < right) or (right < mid and mid < left):
        return mid_in
    elif (left < right and right < mid) or (right < left and mid < right):
        return end_index
    else:
        return start_index


# Optimize to where here will still search
def quicksort(array, start_index, end_index):
    if start_index >= end_index:
        return

    pivot_in = get_pivot_index(array, start_index, end_index)
    while True:
        curr_pivot = pivot_in
        for i in range(start_index, pivot_in):
            if array[pivot_in] < array[i]:
                array[i], array[pivot_in] = array[pivot_in], array[i]
                pivot_in = i
                break

        for i in range(end_index, pivot_in, -1):
            if array[pivot_in] > array[i]:
                array[i], array[pivot_in] = array[pivot_in], array[i]
                pivot_in = i
                break

        if pivot_in == curr_pivot:
            break

    quicksort(array, start_index=start_index, end_index=pivot_in - 1)
    quicksort(array, start_index=pivot_in + 1, end_index=end_index)
        
    
    
if __name__ == '__main__':
    test = [3, 6, 4, 8, 1, 5, -1, 5, 93, 20]
    quicksort(test, 0, len(test) - 1)
    print(test)