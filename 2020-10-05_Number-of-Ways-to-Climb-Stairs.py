"""
Hi, here's your problem today. This problem was recently asked by LinkedIn:

You are given a positive integer N which represents the number of steps in a staircase. You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.
"""

def staircase(n):
    """Determine the number of ways to climb a total number of n (input) stair \
    if either 1 or 2 steps can be clibed at a time"""
    d=dict()
    d[0]=0
    d[1]=1
    d[2]=2
    for i in range(3,n+1):
        d[i]=d[i-1]+d[i-2]
    return d[n]


print (staircase(4))
# 5
print (staircase(100))
# 8
