# https://leetcode.com/problems/product-of-array-except-self/solution/

def product_except_self(nums):
    result = [1] * len(nums)

    mul = 1
    for i in range(len(nums) - 2, -1, -1):
        mul *= nums[i+1]
        result[i] = mul

    mul = 1
    for i in range(1, len(nums)):
        mul *= nums[i-1]
        result[i] *= mul

    return result
