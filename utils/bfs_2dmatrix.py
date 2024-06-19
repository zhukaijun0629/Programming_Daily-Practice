from typing import List
from collections import deque


class Solution:
    def shortestPath(self, matrix: List[List[int]]) -> int:
        if not matrix or matrix[0][0] == 1 or matrix[-1][-1] == 1:
            return -1

        ROWS, COLS = len(matrix), len(matrix[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        queue = deque([(0, 0, 0)])
        visited = set((0, 0))

        while queue:
            r, c, dist = queue.popleft()

            if r == ROWS - 1 and c == COLS - 1:
                return dist

            for dir_r, dir_c in directions:
                next_r, next_c = r + dir_r, c + dir_c
                if 0 <= next_r < ROWS and 0 <= next_c < COLS and matrix[next_r][next_c] != 1 and (next_r, next_c) not in visited:
                    visited.add((next_r, next_c))
                    queue.append((next_r, next_c, dist + 1))
        return -1

    def shortestPath2(self, matrix: List[List[int]]) -> int:
        if not matrix or matrix[0][0] == 1 or matrix[-1][-1] == 1:
            return -1

        ROWS, COLS = len(matrix), len(matrix[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        start_node = (0, 0)
        queue = deque([start_node])
        visited = set(start_node)
        dist = -1

        while queue:
            dist += 1
            next_queue = []
            for node in queue:
                (r, c) = node
                if r == ROWS - 1 and c == COLS - 1:
                    return dist
                for dir_r, dir_c in directions:
                    next_r, next_c = r + dir_r, c + dir_c
                    if 0 <= next_r < ROWS and 0 <= next_c < COLS and matrix[next_r][next_c] != 1 and (next_r, next_c) not in visited:
                        next_node = (next_r, next_c)
                        visited.add(next_node)
                        next_queue.append(next_node)
            queue = next_queue

        return -1


# Test case
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
maze2 = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

print(Solution().shortestPath(maze))  # Output: 8
print(Solution().shortestPath2(maze))  # Output: 8
print(Solution().shortestPath(maze2))  # Output: 7
print(Solution().shortestPath2(maze2))  # Output: 7
