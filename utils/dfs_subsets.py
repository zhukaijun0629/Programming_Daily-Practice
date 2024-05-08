class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        if not nums:
            return [[]]

        results = []
        self.dfs(nums, 0, [], results)
        return results

    def dfs(self, nums, index, candidate, results):
        results.append(candidate[:])

        for i in range(index, len(nums)):
            candidate.append(nums[i])
            self.dfs(nums, i + 1, candidate, results)
            candidate.pop()


print(Solution().subsets([1, 2, 3]))
