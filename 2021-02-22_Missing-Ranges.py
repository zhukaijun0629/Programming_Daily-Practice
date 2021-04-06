"""
Hi, here's your problem today. This problem was recently asked by Google:

Given a sorted list of numbers, and two integers low and high representing the lower and upper bound of a range, return a list of (inclusive) ranges where the numbers are missing. A range should be represented by a tuple in the format of (lower, upper).
"""


def missing_ranges(nums, low, high):
    # Fill this in.
    if not nums:
        return [(low, high)]
    res = []
    
    if low < nums[0]:
        res.append((low, nums[0] - 1))
    
    for i in range(len(nums) - 1):
        if nums[i] + 1 < nums[i + 1]:
            res.append((nums[i] + 1, nums[i + 1] - 1))
            
    if high > nums[-1]:
        res.append((nums[-1] + 1, high))

    return res



print(missing_ranges([1, 3, 5, 10], 1, 10))
# [(2, 2), (4, 4), (6, 9)]
print(missing_ranges([2, 3, 5, 9], 1, 10))
# [(1, 1), (4, 4), (6, 8),(10, 10)]