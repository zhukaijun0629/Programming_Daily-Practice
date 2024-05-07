"""
Hi, here's your problem today. This problem was recently asked by Amazon:

You are given a 2D array of integers. Print out the clockwise spiral traversal of the matrix.

Example:

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

The clockwise spiral traversal of this array is:

1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12
"""

def matrix_spiral_print(matrix):
    return matrix and list(matrix.pop(0)) + matrix_spiral_print(list(zip(*matrix))[::-1])

    # L=[]
    # def direct_print(M,D):
    #     if not M:
    #         return
    #     else:
    #         if D=="R":
    #             for i in M[0]:
    #                 print(i)
    #                 L.append(i)
    #             direct_print(M[1:],"D")
    #         if D=="D":
    #             for i in [row[-1] for row in M]:
    #                 print(i)
    #                 L.append(i)
    #             direct_print([row[:-1] for row in M],"L")
    #         if D=="L":
    #             for i in reversed(M[-1]):
    #                 print(i)
    #                 L.append(i)
    #             direct_print(M[:-1],"U")
    #         if D=="U":
    #             for i in reversed([row[0] for row in M]):
    #                 print(i)
    #                 L.append(i)
    #             direct_print([row[1:] for row in M],"R")
    #
    # direct_print(M,"R")
    # print(L)



grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

print(matrix_spiral_print(grid))
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
