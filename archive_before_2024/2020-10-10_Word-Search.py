"""
Hi, here's your problem today. This problem was recently asked by Amazon:

You are given a 2D array of characters, and a target string. Return whether or not the word target word exists in the matrix. Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix.

Example:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

Given this matrix, and the target word FOAM, you should return true, as it can be found going up-to-down in the first column.
"""

def word_search(board, word):
    vis = set()
    n, m = len(board), len(board[0])
    def word_exists(row, col, p):
        if p == len(word):
            return True

        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ci, cj = i + row, j + col
            if 0 <= ci < n and  0 <= cj < m and (ci, cj) not in vis and board[ci][cj] == word[p]:
                vis.add((ci, cj))
                if word_exists(ci, cj, p+1):
                    return True

                vis.remove((ci, cj))

        return False

    for i in range(n):
        for j in range(m):
            if board[i][j] == word[0]:
                vis.add((i, j))
                if word_exists(i, j, 1):
                    return True
                vis.remove((i, j))

    return False

matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]
print (word_search(matrix, 'CQOB'))
# True
