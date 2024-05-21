'''
1863. Sum of All Subset XOR Totals

The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums. 

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

Constraints:

1 <= nums.length <= 12
1 <= nums[i] <= 20
'''

from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        results = []
        self.dfs(sorted(nums), 0, [], results)
        return sum(results)

    def dfs(self, nums, index, candidate, results):
        results.append(self.XORAllElements(candidate[:]))

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            candidate.append(nums[i])
            self.dfs(nums, i+1, candidate, results)
            candidate.pop()

        return results

    def XORAllElements(self, nums):
        ans = 0
        for num in nums:
            ans ^= num
        return ans


print(Solution().subsetXORSum([1, 2, 2]))
print(Solution().subsetXORSum([1, 1, 1]))
