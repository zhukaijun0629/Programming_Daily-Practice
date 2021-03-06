"""
Hi, here's your problem today. This problem was recently asked by Apple:

Given a binary tree, return the list of node values in zigzag order traversal.
Here's an example

# Input:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
#
# Output: [1, 3, 2, 4, 5, 6, 7]
"""

import collections


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def zigzag_order(tree):
    # Fill this in.
    if not tree:
        return []

    queue = collections.deque([tree])
    inorder = True
    res = []
    while queue:
        res_level = []
        next_queue = []
        for node in queue:
            res_level.append(node.value)
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        if inorder:
            res.extend(res_level)
        else:
            res.extend(res_level[::-1])

        queue = next_queue
        inorder = not inorder

    return res


n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n2 = Node(2, n4, n5)
n3 = Node(3, n6, n7)
n1 = Node(1, n2, n3)

print(zigzag_order(n1))
# [1, 3, 2, 4, 5, 6, 7]
