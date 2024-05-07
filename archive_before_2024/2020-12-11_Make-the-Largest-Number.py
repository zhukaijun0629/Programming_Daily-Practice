"""
Hi, here's your problem today. This problem was recently asked by Uber:

Given a number of integers, combine them so it would create the largest number.

Example:
Input:  [17, 7, 2, 45, 72]
Output:  77245217

Leetcode #179
"""


class LargerNumKey(str):
    def __lt__(x, y):
        return x+y < y+x
# Here we override __lt__ to compare x+y vs y+x instead since
# __lt__ is used as default sort method 

class Solution:
    def largestNum(self, nums):
        nums= list(map(str, nums))
        nums.sort(key = LargerNumKey,reverse= True)
        largest_num = ''.join(nums)
        return '0' if largest_num[0] == '0' else largest_num

print (Solution().largestNum([17, 72, 2, 45, 7]))
# 77245217
