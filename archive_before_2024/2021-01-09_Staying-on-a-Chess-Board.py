"""
Hi, here's your problem today. This problem was recently asked by Google:

A chess board is an 8x8 grid. Given a knight at any position (x, y) and a number of moves k, we want to figure out after k random moves by a knight, the probability that the knight will still be on the chessboard. Once the knight leaves the board it cannot move again and will be considered off the board.

Leetcode #688
"""
from collections import defaultdict

def is_knight_on_board(x, y, k, cache={}):
    # Fill this in.
    if k == 0:
        return sum(list(cache.values()))
    new_cache = defaultdict(int)
    if not cache:
        cache[(x,y)] = 1
    for (pre_x, pre_y),prob in cache.items():
        for dx, dy in [(1,2),(2,1),(-1,-2),(-2,-1),(1,-2),(2,-1),(-1,2),(-2,1)]:
            if 0 <= pre_x + dx < 8 and 0 <= pre_y + dy < 8:
                new_cache[(pre_x + dx, pre_y + dy)] += prob / 8
    return is_knight_on_board(0, 0, k-1, new_cache)



print (is_knight_on_board(0, 0, 1))
# 0.25
