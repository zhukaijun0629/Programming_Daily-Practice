"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

You 2 integers n and m representing an n by m grid, determine the number of ways you can get from the top-left to the bottom-right of the matrix y going only right or down.

Example:
n = 2, m = 2

This should return 2, since the only possible routes are:
Right, down
Down, right.
"""

#Solution 1
# def num_ways(m, n):
    # dp=[[0 for i in range(n+1)] for j in range(m+1)]
    # # print(dp)
    # for i in range(1,m+1):
    #     for j in range(1,n+1):
    #         if i==1 or j==1:
    #             dp[i][j]=1
    #         else:
    #             dp[i][j]=dp[i-1][j]+dp[i][j-1]
    # return dp[m][n]

#Solution 2
class Solution2:
    def __init__(self):
        self.wayAtPos={}
    def num_ways(self,m,n):
        if (m,n) in self.wayAtPos:
            return self.wayAtPos[(m,n)]
        if m<1 or n<1:
            return 0
        if m==1 or n==1:
            return 1
        self.wayAtPos[(m,n)]= self.num_ways(m-1,n) + self.num_ways(m,n-1)
        return self.wayAtPos[(m,n)]

print (Solution2().num_ways(3,7))
# 2
