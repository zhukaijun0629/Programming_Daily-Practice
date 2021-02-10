"""
Hi, here's your problem today. This problem was recently asked by Apple:

A fixed point in a list is where the value is equal to its index. So for
example the list [-5, 1, 3, 4], 1 is a fixed point in the list since the index
and value is the same. Find a fixed point (there can be many, just return 1) in
a sorted list of distinct elements, or return None if it doesn't exist.
"""


def find_fixed_point(nums):
    if not nums:
        return None

    start = 0
    end = len(nums) - 1

    while start + 1 < end:
        mid = (start + end) // 2
        if nums[mid] > mid:
            end = mid
        elif nums[mid] < mid:
            start = mid
        else:
            return mid

    if nums[start] == start:
        return start
    if nums[end] == end:
        return end

    return None


print(find_fixed_point([-5, 1, 3, 4, 5]))
# 1
