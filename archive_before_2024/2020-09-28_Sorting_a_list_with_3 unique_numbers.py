"""
Hi, here's your problem today. This problem was recently asked by Google:

Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

Example 1:
Input: [3, 3, 2, 1, 3, 2, 1]
Output: [1, 1, 2, 2, 3, 3, 3]
"""

def sortNums(nums):
    mid = 2
    left = 0
    right = len(nums)-1
    i=0

    while i<right:
        if nums[i]<mid:
            nums[left],nums[i]=nums[i],nums[left]
            left+=1
            i+=1
        elif nums[i]>mid:
            nums[i],nums[right]=nums[right],nums[i]
            right-=1
        else:
            i+=1
    return nums



print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]
