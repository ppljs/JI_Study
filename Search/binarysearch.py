def binary_search(array, target, start, end):
    mid = (end + start) // 2

    if start > end:
        return -1

    if  target > array[mid]:
        return binary_search(array, target, mid + 1, end)
    elif target < array[mid]:
        return binary_search(array, target, start, mid - 1)
    else:
        return mid


if __name__ == '__main__':
    sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = binary_search(sorted_arr, 8, 0, len(sorted_arr) - 1)
    print(result)