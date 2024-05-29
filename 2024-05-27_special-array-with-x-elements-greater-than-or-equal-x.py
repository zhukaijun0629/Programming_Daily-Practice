'''
1608. Special Array With X Elements Greater Than or Equal X

You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
'''

from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        if nums[-1] >= n:
            return n
        for i in range(1, n):
            if nums[i-1] >= i and nums[i] < i:
                return i
        return -1


# [0,4,3,0,4] 4,4,3,0,0
# [3,5] 5,3

print(Solution().specialArray([0, 4, 3, 0, 4]))
print(Solution().specialArray([3, 5]))
print(Solution().specialArray([3, 6, 7, 7, 0]))
