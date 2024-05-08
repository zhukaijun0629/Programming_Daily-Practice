class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        if not nums:
            return [[]]
        
        results = []
        self.dfs(nums, set(), [], results)
        return results
    
    def dfs(self,nums, visited, candidate, results):
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

print(Solution().permute([1, 2, 3]))
