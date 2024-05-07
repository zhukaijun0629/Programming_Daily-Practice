"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution:
    def moveZeros(self, nums):
        # Fill this in.
############ Method1
        # i=0
        # j=len(nums)
        # while i<j:
        #     if nums[i]==0:
        #         nums.pop(i)
        #         nums.append(0)
        #         j-=1
        #     else:
        #         i+=1
        # return nums

############ Method2
        zeropos = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[zeropos],nums[i]=nums[i],nums[zeropos]
                zeropos+=1



# nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
nums = [0,1,0,3,12]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
