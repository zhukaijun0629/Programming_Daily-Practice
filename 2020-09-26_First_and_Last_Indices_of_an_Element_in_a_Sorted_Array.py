"""
Hi, here's your problem today. This problem was recently asked by AirBNB:

Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.
"""

class Solution:
  def getRange(self, arr, target):
    # Fill this in.
    d=dict()
    for i,v in enumerate(arr):
        if v in d:
            d[v].append(i)
        else:
            d[v]=[i]
    res=d.get(target)
    if res==None:
        return [-1,-1]
    else:
        return [res[0],res[-1]]

# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 0
print(Solution().getRange(arr, x))
# [1, 4]
