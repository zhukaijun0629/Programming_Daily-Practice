"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given an array of integers of size n, where all elements are between 1 and n inclusive, find all of the elements of [1, n] that do not appear in the array. Some numbers may appear more than once.

Example:
Input: [4,5,2,6,8,2,1,5]
Output: [3,7]

For this problem, you can assume that you can mutate the input array.
"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        # Fill this in.
        l = len(nums)
        res = []
        nums = set(nums)
        for i in range(1,l+1):
            if i not in nums:
                res.append(i)
        return res

nums = [4, 6, 2, 6, 7, 2, 1]
print(Solution().findDisappearedNumbers(nums))
# [3, 5]
