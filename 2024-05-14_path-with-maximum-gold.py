'''
1219. Path with Maximum Gold

In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
'''

from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def traverse(i, j):
            if (i, j) in visited:
                return 0
            visited.add((i, j))
            cur_gold = grid[i][j]
            future_gold = 0
            for direction in directions:
                next_i = i + direction[0]
                next_j = j + direction[1]
                if 0 <= next_i < ROWS and 0 <= next_j < COLS:
                    if grid[next_i][next_j] == 0:
                        visited.add((next_i, next_j))
                        continue
                    future_gold = max(future_gold, traverse(next_i, next_j))
            visited.discard((i, j))
            return cur_gold + future_gold

        result = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    visited.add((i, j))
                    continue
                result = max(result, traverse(i, j))
        return result


# DFS to visit each cell once, store the result with max gold
print(Solution().getMaximumGold([[0, 6, 0], [5, 8, 7], [0, 9, 0]]))
