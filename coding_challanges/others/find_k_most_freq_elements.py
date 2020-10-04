def find_k_most_frequent_elements_in_array(arr, k):
    frequency_map = build_frequency_hash_map(arr)
    sorted_num_frequency_pairs = sorted(create_keyvalue_pairs(frequency_map), key=lambda pair: pair[1], reverse=True)

    return [num_freq_pair[0] for index, num_freq_pair in enumerate(sorted_num_frequency_pairs) if index < k]


def build_frequency_hash_map(arr):
    frequency_map = {}
    for num in arr:
        if num not in frequency_map:
            frequency_map[num] = 0
        frequency_map[num] += 1

    return frequency_map


def create_keyvalue_pairs(hash_map):
    return list(hash_map.items())


if __name__ == '__main__':
    # test_arr = [1,1,2,3,1,4,3,2,5]
    # test_arr = [1,1,2,3,1,4,3,2,5,5,5,5,5]
    test_arr = []
    k = 3
    print(find_k_most_frequent_elements_in_array(test_arr, k))
