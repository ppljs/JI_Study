def group_anagrams(strs):
    anagram_groups = {}
    for curr_str in strs:
        count_arr = string_to_count_string(curr_str)
        if count_arr not in anagram_groups:
            anagram_groups[count_arr] = [curr_str]
        else:
            anagram_groups[count_arr].append(curr_str)

    return [a_group for a_key, a_group in anagram_groups.items()]


def string_to_count_string(s):
    count_arr = [0] * 26
    for c in s:
        index = ord(c) - ord('a')
        count_arr[index] += 1

    return ','.join(map(str, count_arr))
