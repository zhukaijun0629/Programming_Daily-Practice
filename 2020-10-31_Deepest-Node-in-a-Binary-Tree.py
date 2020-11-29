"""
Hi, here's your problem today. This problem was recently asked by Google:

You are given the root of a binary tree. Return the deepest node (the furthest node from the root).

Example:

    a
   / \
  b   c
 /
d

The deepest node in this tree is d at depth 3.
"""

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        # string representation
        return self.val


def deepest(node):
    # Fill this in.
    if not node:
        return 0
    pq=[(root,1)]
    while pq:
        s,k=pq.pop(0)
        if s.left:
            pq.append((s.left,k+1))
        if s.right:
            pq.append((s.right,k+1))
    return (s,k)


root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print (deepest(root))
# (d, 3)
