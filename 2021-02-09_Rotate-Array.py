"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Given an array and an integer k, rotate the array by k spaces. Do this without generating a new array and without using extra space.
"""


def rotate_list(nums, k):
    # Fill this in.
    
    def helper(nums, end_idx, k):
        for i in range(k - 1, -1, -1):
            nums[end_idx], nums[i] = nums[i], nums[end_idx]
            end_idx -= 1
        if k % (end_idx + 1):
            helper(nums, end_idx, k % (end_idx + 1))
    if k % len(nums):
        helper(nums, len(nums) - 1, k)

a = [1, 2, 3, 4, 5]
rotate_list(a, 5)
print(a)
# [3, 4, 5, 1, 2]
