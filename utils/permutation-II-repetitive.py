from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        results = []
        self.dfs(nums, [0]*len(nums), [], results)
        return results
    
    def dfs(self, nums: List[int], visited: List[bool], candidate: List[int], results: List[List[int]]):
        if len(candidate) == len(nums):
            results.append(candidate[:])
            return
        
        for i, num in enumerate(nums):
            if visited[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue

            candidate.append(num)
            visited[i] = True

            self.dfs(nums, visited, candidate, results)

            candidate.pop()
            visited[i] = False

print(Solution().permute([1,2,2,2]))