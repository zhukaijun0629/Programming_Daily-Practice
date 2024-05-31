'''
2597. The Number of Beautiful Subsets

You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

Constraints:

1 <= nums.length <= 20
1 <= nums[i], k <= 1000
'''

from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        results = []
        self.dfs(nums, k, 0, [], results)
        return len(results)

    def dfs(self, nums, k, index, candidate, results):
        if candidate:
            results.append(candidate[:])

        for i in range(index, len(nums)):
            cur_num = nums[i]
            if self.isNumGood(cur_num, k, candidate):
                candidate.append(nums[i])
                self.dfs(nums, k, i+1, candidate, results)
                candidate.pop()

    def isNumGood(self, num, k, candidate):
        for n in candidate:
            if abs(n - num) == k:
                return False
        return True
