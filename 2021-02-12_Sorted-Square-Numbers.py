"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

Given a list of sorted numbers (can be both negative or positive), return the list of numbers squared in sorted order.

Solve this problem in O(n) time.
"""


def square_numbers1(nums):
    # Fill this in.
    # O(nlogn)
    return sorted([n ** 2 for n in nums])

def square_numbers2(nums):
    res = []
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] ** 2 > nums[right] ** 2:
            res.append(nums[left] ** 2)
            left += 1
        else:
            res.append(nums[right] ** 2)
            right -= 1
    return res[::-1]



print(square_numbers2([-5, -3, -1, 0, 1, 4, 5]))
# [0, 1, 1, 9, 16, 25, 25]
