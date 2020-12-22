"""
Hi, here's your problem today. This problem was recently asked by Facebook:

You are given an array of integers. Return all the permutations of this array.
"""

def permute(nums):
    # Fill this in.
    if not nums:
        return [[]]
    res = []
    for i,n in enumerate(nums):
        pre_res = permute(nums[:i]+nums[i+1:])
        for x in pre_res:
            res.append([n]+x)
    return res


print (permute([1, 2, 3]))
# [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
