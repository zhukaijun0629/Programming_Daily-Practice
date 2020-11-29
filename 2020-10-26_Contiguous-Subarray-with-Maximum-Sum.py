"""
Hi, here's your problem today. This problem was recently asked by Twitter:

You are given an array of integers. Find the maximum sum of all possible contiguous subarrays of the array.

Example:

[34, -50, 42, 14, -5, 86]

Given this input array, the output should be 137. The contiguous subarray with the largest sum is [42, 14, -5, 86].

Your solution should run in linear time.
"""

def max_subarray_sum(nums):
    """Leetcode 53. Maximum Subarray"""
    # Fill this in.
    if not nums:
        return
    bst=None
    cur=None
    for num in nums:
        if bst==None:
            bst=num
            cur=num
        else:
            cur=max(cur+num,num)
            bst=max(bst,cur)
    return bst

print (max_subarray_sum([34, -50, 42, 14, -5, 86]))
# 137
