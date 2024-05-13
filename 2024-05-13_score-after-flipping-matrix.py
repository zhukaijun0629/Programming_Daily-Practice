'''
861. Score After Flipping Matrix

You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid[i][j] is either 0 or 1.
'''

from typing import List

class Solution:
    def matrixScore2(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            if grid[r][0] == 0:
                for c in range(COLS):
                    grid[r][c] = 1 - grid[r][c]
        results = 0
        for c in range(COLS):
            sum_col = 0
            for r in range(ROWS):
                sum_col += grid[r][c]
            results = 2*results + max(sum_col, ROWS - sum_col)
        return results
    
### 1000 > 111
print(Solution().matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))