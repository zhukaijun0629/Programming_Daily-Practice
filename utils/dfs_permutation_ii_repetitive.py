class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        if not nums:
            return [[]]

        results = []
        self.dfs(sorted(nums), [0]*len(nums), [], results)
        return results

    def dfs(self, nums, visited, candidate, results):
        if len(nums) == len(candidate):
            results.append(candidate[:])
            return

        for i, num in enumerate(nums):
            if visited[i]:
                continue
            # never add a repeated number prior to its first apperance
            if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue

            candidate.append(num)
            visited[i] = True

            self.dfs(nums, visited, candidate, results)

            visited[i] = False
            candidate.pop()


print(Solution().permute([1, 2, 2, 2]))
