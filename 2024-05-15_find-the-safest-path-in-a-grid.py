'''
2812. Find the Safest Path in a Grid

You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:

A cell containing a thief if grid[r][c] = 1
An empty cell if grid[r][c] = 0
You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.

Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.

The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.

Constraints:

1 <= grid.length == n <= 400
grid[i].length == n
grid[i][j] is either 0 or 1.
There is at least one thief in the grid.
'''
from typing import List
from heapq import heappop, heappush
from collections import deque


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        queue = []
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    queue.append(((r, c), 0))
                    visited.add((r, c))
        while queue:
            next_queue = []
            for (r, c), distance in queue:
                for direction in directions:
                    next_r = r + direction[0]
                    next_c = c + direction[1]
                    if 0 <= next_r < ROWS and 0 <= next_c < COLS and grid[next_r][next_c] == 0:
                        grid[next_r][next_c] = distance - 1
                        next_queue.append(((next_r, next_c), distance-1))
            queue = next_queue

        maxHeap = [(grid[0][0], (0, 0))]
        while maxHeap:
            distance, (r, c) = heappop(maxHeap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if r == ROWS - 1 and c == COLS - 1:
                return -distance
            for direction in directions:
                next_r = r + direction[0]
                next_c = c + direction[1]
                if 0 <= next_r < ROWS and 0 <= next_c < COLS and (next_r, next_c) not in visited:
                    heappush(
                        maxHeap, (max(distance, grid[next_r][next_c]), (next_r, next_c)))
        return 0

    def maximumSafenessFactor2(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    queue.append(((r, c), 0))
                    visited.add((r, c))
        while queue:
            (r, c), distance = queue.popleft()
            for direction in directions:
                next_r = r + direction[0]
                next_c = c + direction[1]
                if 0 <= next_r < ROWS and 0 <= next_c < COLS and grid[next_r][next_c] == 0:
                    grid[next_r][next_c] = distance - 1
                    queue.append(((next_r, next_c), distance-1))

        maxHeap = [(grid[0][0], (0, 0))]
        while maxHeap:
            distance, (r, c) = heappop(maxHeap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if r == ROWS - 1 and c == COLS - 1:
                return -distance
            for direction in directions:
                next_r = r + direction[0]
                next_c = c + direction[1]
                if 0 <= next_r < ROWS and 0 <= next_c < COLS and (next_r, next_c) not in visited:
                    heappush(
                        maxHeap, (max(distance, grid[next_r][next_c]), (next_r, next_c)))
        return 0


'''
0   0   0   0   0
1   0   1   1   0
0   0   0   0   0
0   1   1   1   1
0   0   0   0   0

-1  -2  -1   -1   -1
1   -1   1   1   -1
-1  -1  -1   -1  -1
-1   1   1   1   1
-2   -1   -1  -1  -1
'''
print(Solution().maximumSafenessFactor2(
    [[0, 0, 0, 0, 0],
     [1, 0, 1, 1, 0],
     [0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1],
     [0, 0, 0, 0, 0]]))

'''
0   0   0
0   0   1
0   0   0

-3   -2   -1
-2   -1   1
-3   -2   -1
'''
print(Solution().maximumSafenessFactor2([[0, 0, 0], [0, 0, 1], [0, 0, 0]]))

'''
0   0   0
0   0   1
1   0   0

-2   -2   -1
-1   -1   1
1   -1   -1
'''
print(Solution().maximumSafenessFactor2([[0, 0, 0], [0, 0, 1], [1, 0, 0]]))

'''
0   1   1
1   1   1
1   1   0
'''
