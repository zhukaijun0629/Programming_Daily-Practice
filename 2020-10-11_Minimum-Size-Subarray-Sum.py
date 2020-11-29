"""
Hi, here's your problem today. This problem was recently asked by Amazon:

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
"""

class Solution:
    def minSubArrayLen(self, nums, s):
        if not nums:
            return 0
        i=j=0
        res=len(nums)+1
        total=0
        while i < len(nums):
            while total < s and j < len(nums):
                total+=nums[j]
                j+=1
            if total>=s:
                res = min(res,j-i)
                total-=nums[i]
            i+=1
        return res%(len(nums)+1)





print (Solution().minSubArrayLen([], 100))
# 2
