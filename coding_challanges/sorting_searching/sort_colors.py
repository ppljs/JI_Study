# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/798/
 """
Given an array with n objects colored red, white or blue, sort them in-place so that objects of
the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.
 """


# PS: I know that I've came to an overly complicated solution .... hahahahaha

def sort_colors(self, nums: List[int]) -> None:
    for tar_num in range(2, 0, -1):
        left, right = 0, len(nums) - 1
        while left < right:
            curr_num = nums[left]
            if curr_num == tar_num:
                if curr_num > nums[right]:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
                else:
                    right -= 1
            else:
                left += 1
