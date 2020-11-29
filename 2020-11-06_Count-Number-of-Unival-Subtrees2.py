"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

A unival tree is a tree where all the nodes have the same value. Given a binary tree, return the number of unival subtrees in the tree.

For example, the following tree should return 5:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

The 5 trees are:
- The three single '1' leaf nodes. (+3)
- The single '0' leaf node. (+1)
- The [1, 1, 1] tree at the bottom. (+1)
"""

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_unival_subtrees(root):
    # Fill this in.
    count = [0]
    isUnivalTree(root,count)
    return count[0]


def isUnivalTree(root,count):
    if not root:
        return True
    left = isUnivalTree(root.left,count)
    right = isUnivalTree(root.right,count)
    if left == False or right == False:
        return False
    if root.left and root.val!=root.left.val:
        return False
    if root.right and root.val!=root.right.val:
        return False
    count[0]+=1
    return True




a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print (count_unival_subtrees(a))
# 5
