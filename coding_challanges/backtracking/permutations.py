def permute(nums):
    nums = set(nums)
    result = []
    curr_per = []
    do_permute(nums, result, curr_per)

    return result


def do_permute(nums, result, curr_per):
    if not nums:
        result.append(curr_per.copy())

    for num in nums:
        curr_per.append(num)
        do_permute(nums.difference({num}), result, curr_per)
        curr_per.pop()