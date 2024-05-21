'''
78. Subsets

Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        results = []
        self.dfs(nums, 0, [], results)
        return results

    def dfs(self, nums, index, candidate, results):
        results.append(candidate[:])

        for i in range(index, len(nums)):
            candidate.append(nums[i])
            self.dfs(nums, i+1, candidate, results)
            candidate.pop()


print(Solution().subsets([0, 1]))
print(Solution().subsets([0, 1, 2]))
