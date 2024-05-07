"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given an array, nums, of n integers, find all unique triplets (three numbers, a, b, & c) in nums such that a + b + c = 0. Note that there may not be any triplets that sum to zero in nums, and that the triplets must not be duplicates.
"""

class Solution(object):
    def threeSum(self, nums):
        # Fill this in.
        ans={}
        if len(nums)<3:
            return []
        nums.sort()
        if nums[-1]<0:
            return []
        while len(nums)>=3 and nums[0]<=0:
            a=nums.pop()
            target = -a
            if nums[-1]+nums[-2]<target:
                continue
            i=0
            j=len(nums)-1
            while i<j:
                if nums[i]+nums[j]==target:
                    ans[(a,nums[i],nums[j])]=True
                    i+=1
                    j-=1
                elif nums[i]+nums[j]<target:
                    i+=1
                else:
                    j-=1
        return [list(key) for key in ans.keys()]




# Test Program
nums = [1, -2, 1, 0, 5]
print(Solution().threeSum(nums))
# [[-2, 1, 1]]
