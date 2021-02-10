"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given a tree, find if the binary tree is height balanced or not. A height
balanced binary tree is a tree where every node's 2 subtree do not differ
in height by more than 1.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_height_balanced(tree):
    # Fill this in.
    def helper(node, level=0):
        if not node:
            return True, level
        is_left_balanced, left_level = helper(node.left, level + 1)
        is_right_balanced, right_level = helper(node.right, level + 1)
        return is_left_balanced and is_right_balanced and \
            abs(left_level - right_level) <= 1, \
            max(left_level, right_level)
    return helper(tree)[0]


def is_height_balanced2(tree):
    # Fill this in.
    def get_level(node):
        if not node:
            return 0
        return 1 + max(get_level(node.left), get_level(node.right))

    if not tree:
        return True
    return abs(get_level(tree.left) - get_level(tree.right)) <= 1 and \
        is_height_balanced2(tree.left) and is_height_balanced2(tree.right)

    #     1
    #    / \
    #   2   3
    #  /
    # 4
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4)
n1 = Node(1, n2, n3)

# print(is_height_balanced(n1))
print(is_height_balanced2(n1))
# True


#     1
#    /
#   2
#  /
# 4
n1 = Node(1, n2)
# print(is_height_balanced(n1))
print(is_height_balanced2(n1))
# False
