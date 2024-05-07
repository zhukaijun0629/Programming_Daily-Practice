"""
Hi, here's your problem today. This problem was recently asked by Facebook:

A Sudoku board is a 9x9 grid, where each row, column and each 3x3 subbox contains the number from 1-9. Here's an example of a Sudoku board.
-------------
|534|678|912|
|672|195|348|
|198|342|567|
|------------
|859|761|423|
|426|853|791|
|713|924|856|
|------------
|961|537|284|
|287|419|635|
|345|286|179|
|------------

Given a 9x9 board, determine if it is a valid Sudoku board. The board may be partially filled, where an empty cell will be represented by the space character ' '.
"""


class Solution:
    def isValidSudoku(self, board):
        if not self.checkRows(board):
            return False
        if not self.checkCols(board):
            return False
        if not self.checkBlocks(board):
            return False
        
        return True
    
    def checkRows(self, board):
        ROWS = len(board)
        COLS = len(board[0])
        for r in range(ROWS):
            candidates = []
            for c in range(COLS):
                candidates.append(board[r][c])
            if not self.checkUnit(candidates):
                return False
        return True
    
    def checkCols(self, board):
        ROWS = len(board)
        COLS = len(board[0])
        for c in range(COLS):
            candidates = []
            for r in range(ROWS):
                candidates.append(board[r][c])
            if not self.checkUnit(candidates):
                return False
        return True
    
    def checkBlocks(self, board):
        base = [(r, c) for r in [0,3,6] for c in [0,3,6]]
        for br, bc in base:
            candidates = []
            for dr in range(3):
                for dc in range(3):
                    candidates.append(board[br+dr][bc+dc])
            if not self.checkUnit(candidates):
                return False
        return True
    
    def checkUnit(self, candidates):
        unit_set = set()
        for item in candidates:
            if item == ' ':
                continue
            if item in unit_set:
                return False
            unit_set.add(item)
        return True




board = [
    [5, ' ', 4, 6, 7, 8, 9, 1, 2],
    [6, ' ', 2, 1, 9, 5, 3, 4, 8],
    [1,   9, 8, 3, 4, 2, 5, 6, 7],
    [8,   5, 9, 7, 6, 1, 4, 2, 3],
    [4,   2, 6, 8, 5, 3, 7, 9, 1],
    [7,   1, 3, 9, 2, 4, 8, 5, 6],
    [9,   6, 1, 5, 3, 7, 2, 8, 4],
    [2,   8, 7, 4, 1, 9, 6, 3, 5],
    [3,   4, 5, 2, 8, 6, 1, 7, 9],
]

print(Solution().isValidSudoku(board))
# True
