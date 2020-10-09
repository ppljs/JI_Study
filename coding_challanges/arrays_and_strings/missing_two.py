# Cracking the Coding Interview

# Problem: "Missing Two"

# Example:
# Given an array of unique numbers from 1..N, return the two numbers
# that are missing. Do it in O(N) time and O(1) space

def find_missing_two(arr):
    sort_arr_from_1_to_N_inplace(arr)
    return find_two_missing_values(arr)


def sort_arr_from_1_to_N_inplace(arr):
    i = 0
    while i < len(arr):
        correct_index = get_index_from_value(arr[i])
        if correct_index == i or correct_index >= len(arr):
            i += 1
        else:
            arr[correct_index], arr[i] = arr[i], arr[correct_index]


def find_two_missing_values(sorted_arr):
    two_missing_values = [len(sorted_arr) + 1, len(sorted_arr) + 2]
    for index, value in enumerate(sorted_arr):
        expected_value = get_value_from_index(index)
        if value != expected_value:
            if value == two_missing_values[0]:
                two_missing_values[0] = expected_value
            else:
                two_missing_values[1] = expected_value

    return two_missing_values


def get_value_from_index(index):
    return index + 1


def get_index_from_value(value):
    return value - 1


if __name__ == '__main__':
    print( find_missing_two( [5,4,1,3,2,6,7,8] ) )
    print( find_missing_two( [1,3] ) )
