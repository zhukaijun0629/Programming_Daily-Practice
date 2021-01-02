"""
Hi, here's your problem today. This problem was recently asked by Google:

Design a Tic-Tac-Toe game played between two players on an n x n grid. A move is guaranteed to be valid, and a valid move is one placed on an empty block in the grid. A player who succeeds in placing n of their marks in a horizontal, diagonal, or vertical row wins the game. Once a winning condition is reached, the game ends and no more moves are allowed. Below is an example game which ends in a winning condition:

Given n = 3, assume that player 1 is "X" and player 2 is "O"
board = TicTacToe(3);

board.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

board.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

board.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

board.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

board.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

board.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

board.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
"""

class TicTacToe(object):
    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.rowMoveCount1 = [0] * n
        self.rowMoveCount2 = [0] * n
        self.colMoveCount1 = [0] * n
        self.colMoveCount2 = [0] * n
        self.mainDiagMoveCount1 = [0]
        self.mainDiagMoveCount2 = [0]
        self.antiDiagMoveCount1 = [0]
        self.antiDiagMoveCount2 = [0]


    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        assert player == 1 or player == 2

        rowCountList = self.rowMoveCount1 if player == 1 else self.rowMoveCount2
        colCountList = self.colMoveCount1 if player == 1 else self.colMoveCount2
        mainDiagCountList = self.mainDiagMoveCount1 if player == 1 else self.mainDiagMoveCount2
        antiDiagCountList = self.antiDiagMoveCount1 if player == 1 else self.antiDiagMoveCount2

        rowCountList[row] += 1
        colCountList[col] += 1
        if row == col:
            mainDiagCountList[0] += 1
        if row + col == self.n - 1:
            antiDiagCountList[0] += 1

        if self.n in [rowCountList[row], colCountList[col],mainDiagCountList[0],antiDiagCountList[0]]:
            return player
        else:
            return 0


board = TicTacToe(3)
board.move(0, 0, 1)
board.move(0, 2, 2)
board.move(2, 2, 1)
board.move(1, 1, 2)
board.move(2, 0, 1)
board.move(1, 0, 2)
print(board.move(2, 1, 1))
