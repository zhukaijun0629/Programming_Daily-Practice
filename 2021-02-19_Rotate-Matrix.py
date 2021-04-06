"""
Hi, here's your problem today. This problem was recently asked by Uber:

Given a square 2D matrix (n x n), rotate the matrix by 90 degrees clockwise.

Leetcode #48
"""


def rotate(mat):
    # Fill this in.
    n = len(mat[0])
    n_idx = len(mat[0]) - 1
    for r in range(n // 2 + n % 2):
        for c in range(n // 2):
            tmp = mat[n_idx - c][r]
            mat[n_idx - c][r] = mat[n_idx - r][n_idx - c]
            mat[n_idx - r][n_idx - c] = mat[c][n_idx - r]
            mat[c][n_idx - r] = mat[r][c]
            mat[r][c] = tmp
    return mat


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Looks like
# 1 2 3
# 4 5 6
# 7 8 9

# Looks like
# 7 4 1
# 8 5 2
# 9 6 3
print(rotate(mat))
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
