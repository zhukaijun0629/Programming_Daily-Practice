"""
Hi, here's your problem today. This problem was recently asked by Google:

Given a binary tree, find and return the largest path from root to leaf.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def largest_path_sum(tree):
    # Fill this in.
    def dfs(node):
        if not node:
            return 0, []
        left_sum, left_path = dfs(node.left)
        right_sum, right_path = dfs(node.right)
        if left_sum > right_sum:
            return node.val + left_sum, left_path + [node.val]
        else:
            return node.val + right_sum, right_path + [node.val]
    return dfs(tree)[1][::-1]


tree = Node(1)
tree.left = Node(3)
tree.right = Node(2)
tree.right.left = Node(4)
tree.left.right = Node(5)
#    1
#  /   \
# 3     2
#  \   /
#   5 4
print(largest_path_sum(tree))
# [1, 3, 5]
