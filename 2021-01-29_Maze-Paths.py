"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

A maze is a matrix where each cell can either be a 0 or 1. A 0 represents that
the cell is empty, and a 1 represents a wall that cannot be walked through.
You can also only travel either right or down.

Given a nxm matrix, find the number of ways someone can go from the top left
corner to the bottom right corner. You can assume the two corners will always
be 0.

Example:
Input: [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
# 0 1 0
# 0 0 1
# 0 0 0
Output: 2
The two paths that can only be taken in the above example are: down -> right
-> down -> right, and down -> down -> right -> right.
"""


def paths_through_maze(maze):
    row = len(maze)
    col = len(maze[0])
    dp = [[0] * col for _ in range(row)]

    if maze[0][0] == 0:
        dp[0][0] = 1
    else:
        return 0

    for r in range(row):
        for c in range(col):
            if r == 0 and c == 0:
                continue
            if maze[r][c] == 1:
                dp[r][c] = 0
                break
            from_top = dp[r - 1][c] if r > 0 else 0
            from_left = dp[r][c - 1] if c > 0 else 0
            dp[r][c] = from_top + from_left

    return dp[-1][-1]


print(paths_through_maze([[0, 1, 0],
                          [0, 0, 0],
                          [0, 0, 0]]))
# 2
