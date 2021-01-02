"""
Hi, here's your problem today. This problem was recently asked by Twitter:

You are given the root of a binary tree. Find the level for the binary tree with the minimum sum, and return that value.

For instance, in the example below, the sums of the trees are 10, 2 + 8 = 10, and 4 + 1 + 2 = 7. So, the answer here should be 7.
"""
from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def minimum_level_sum(root):
    # Fill this in.
    dq = deque()
    dq.append((root,0))
    cur_level = 0
    cur_sum = 0
    res = root.val
    while dq:
        s,k = dq.popleft()
        if k == cur_level:
            cur_sum+=s.val
        else:
            res=min(res,cur_sum)
            cur_sum=s.val
            cur_level=k
        if s.left:
            dq.append((s.left,k+1))
        if s.right:
            dq.append((s.right,k+1))
    return min(res,cur_sum)


#     10
#    /  \
#   2    8
#  / \    \
# 4   1    2
node = Node(10)
node.left = Node(2)
node.right = Node(8)
node.left.left = Node(4)
node.left.right = Node(1)
node.right.right = Node(2)

print (minimum_level_sum(node))
#7
