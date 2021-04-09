"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

N-Queens is the problem where you find a way to put n queens on a nxn chess board without them being able to attack each other. Given an integer n, return 1 possible solution by returning all the queen's position.
"""

import pprint


def n_queens(n):
    # Fill this in.
    row_set = set()
    col_set = set()
    diag1_set = set()
    diag2_set = set()

    def checkValid(r, c):
        if r in row_set:
            return False
        if c in col_set:
            return False
        if r - c in diag1_set:
            return False
        if r + c in diag2_set:
            return False
        return True

    def markQueen(r, c):
        row_set.add(r)
        col_set.add(c)
        diag1_set.add(r - c)
        diag2_set.add(r + c)

    # board = [[0] * n for _ in range(n)]
    res = []
    for r in range(n):
        for c in range(n):
            # if board[r][c] == 0:
            if checkValid(r, c):
                res.append((r, c))
                markQueen(r, c)
            # else:
            #     board[r][c] = '.'
    return res


pprint.pprint(n_queens(100))
# There can be many answers
# [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]

# Q . . . .
# . . . Q .
# . Q . . .
# . . . . Q
# . . Q . .
