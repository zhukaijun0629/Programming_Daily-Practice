"""
Hi, here's your problem today. This problem was recently asked by Amazon:

Given a binary tree and a given node value, return all of the node's cousins.
Two nodes are considered cousins if they are on the same level of the tree with
different parents. You can assume that all nodes will have their own unique
value.
"""


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution(object):
    def list_cousins(self, tree, val):
        if not tree:
            return []
        cur_level = {tree.value: (tree, None)}
        while cur_level != {}:
            next_level = {}
            if val in cur_level:
                return [node_val for node_val in cur_level \
                                if cur_level[node_val][1] != cur_level[val][1]]
            for node_val, node_props in cur_level.items():
                if node_props[0].left:
                    next_level[node_props[0].left.value] \
                                = (node_props[0].left, node_val)
                if node_props[0].right:
                    next_level[node_props[0].right.value] \
                                = (node_props[0].right, node_val)
            cur_level = next_level
        return []

        #     1
        #    / \
        #   2   3
        #  / \   \
        # 4   6   5


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(6)
root.right = Node(3)
root.right.right = Node(5)

print(Solution().list_cousins(root, 5))
# [4, 6]
