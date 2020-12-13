"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

Given a list of numbers of size n, where n is greater than 3, find the maximum and minimum of the list using less than 2 * (n - 1) comparisons.
"""

def find_min_max(nums):
    # Fill this in.
    if len(nums) == 1:
        return (nums[0],nums[0])
    if len(nums) == 2:
        return (min(nums),max(nums))
    h = len(nums)//2
    l_min, l_max = find_min_max(nums[:h])
    r_min, r_max = find_min_max(nums[h:])
    return (min(l_min,r_min),max(l_max,r_max))

print (find_min_max([3, 5, 1, 2, 4, 8]))
# (1, 8)
