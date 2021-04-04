"""
Hi, here's your problem today. This problem was recently asked by Amazon:

Given a 2d n x m matrix where each cell has a certain amount of change on the floor, your goal is to start from the top left corner mat[0][0] and end in the bottom right corner mat[n - 1][m - 1] with the most amount of change. You can only move either left or down.
"""


def max_change(mat):
    # Fill this in.
    if not mat:
        return 0
    ROWS = len(mat)
    COLS = len(mat[0])
    dp = [[0] * COLS for _ in range(ROWS)]

    for r in range(ROWS):
        for c in range(COLS):
            from_top = dp[r - 1][c] if r - 1 >= 0 else 0
            from_left = dp[r][c - 1] if c - 1 >= 0 else 0
            dp[r][c] = max(from_top, from_left) + mat[r][c]
    
    return dp[ROWS - 1][COLS - 1]


mat = [
    [0, 3, 0, 2],
    [1, 2, 3, 3],
    [6, 0, 3, 2]
]

print(max_change(mat))
# 13
