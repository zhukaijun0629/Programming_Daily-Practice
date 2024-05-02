'''
2441. Largest Positive Integer That Exists With Its Negative

Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.

Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
nums[i] != 0

'''

from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        left_idx = 0
        right_idx = len(nums) - 1
        while left_idx < right_idx:
            if nums[left_idx] == -nums[right_idx]:
                return nums[left_idx]
            if nums[left_idx] > -nums[right_idx]:
                left_idx += 1
            else:
                right_idx -= 1
        return -1


# [3,2,1,-1,-4] shall return 1
print(Solution().findMaxK([3, 2, 1, -1, -4]))
# [3,2,1,-1,-2] shall return 2
print(Solution().findMaxK([3, 2, 1, -1, -2]))
# [3,2,1] shall return -1
print(Solution().findMaxK([3,2,1]))
# [3,2,1,-4] shall return -1
print(Solution().findMaxK([3,2,1,-4]))