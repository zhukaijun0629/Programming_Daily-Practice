"""
Hi, here's your problem today. This problem was recently asked by LinkedIn:

Given a 2-dimensional grid consisting of 1's (land blocks) and 0's (water blocks), count the number of islands present in the grid. The definition of an island is as follows:
1.) Must be surrounded by water blocks.
2.) Consists of land blocks (1's) connected to adjacent land blocks (either vertically or horizontally).
Assume all edges outside of the grid are water.

Example:
Input:
10001
11000
10110
00000

Output: 3
"""

class Solution(object):

    def dfs(self,grid, r,c):
        if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]!= 1:
            return
        grid[r][c] = '#'
        self.dfs(grid, r+1, c)
        self.dfs(grid, r-1, c)
        self.dfs(grid, r, c+1)
        self.dfs(grid, r, c-1)


    def numIslands(self, grid):
        # Fill this in.
        if not grid:
            return 0
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    self.dfs(grid,r,c)
                    ans += 1
        return ans

grid = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0]]
print(Solution().numIslands(grid))
# 3
