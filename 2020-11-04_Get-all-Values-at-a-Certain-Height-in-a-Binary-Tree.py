"""
Hi, here's your problem today. This problem was recently asked by Amazon:

Given a binary tree, return all values given a certain height h.
"""

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def valuesAtHeight(root, height):
    # Fill this in.
    ans=[]
    if not root:
        return None
    queue=[(root,1)]
    while queue:
        s,k = queue.pop(0)
        if k == height:
            ans.append(s.value)
        if k> height:
            break
        if s.left:
            queue.append((s.left,k+1))
        if s.right:
            queue.append((s.right,k+1))

    return ans


#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print (valuesAtHeight(a, 3))
# [4, 5, 7]
