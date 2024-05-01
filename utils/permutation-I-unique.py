from typing import List, Set


class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        results = []
        self.dfs(nums, set(), [], results)
        return results

    def dfs(self, nums: List[int], visited: Set[int], candidate: List[int], results: List[List[int]]):
        if len(candidate) == len(nums):
            results.append(candidate[:])
            return

        for num in nums:
            if num in visited:
                continue

            candidate.append(num)
            visited.add(num)
            self.dfs(nums, visited, candidate, results) 

            candidate.pop()
            visited.remove(num)


print(Solution().permute([1,2,3]))