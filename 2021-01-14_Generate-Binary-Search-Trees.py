"""
Hi, here's your problem today. This problem was recently asked by Amazon:

Given a number n, generate all binary search trees that can be constructed with
nodes 1 to n.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        result = str(self.value)
        if self.left:
            result = result + str(self.left)
        if self.right:
            result = result + str(self.right)
        return result


def generate_bst(n):
    # Fill this in.
    def helper(node_list):
        if not node_list:
            return [None]
        res = []
        for i, root_val in enumerate(node_list):
            left_list = helper(node_list[:i])
            right_list = helper(node_list[i + 1:])
            for left_node in left_list:
                for right_node in right_list:
                    root = Node(root_val)
                    root.left = left_node
                    root.right = right_node
                    res.append(root)
        return res

    node_list = [i for i in range(1, n + 1)]
    res = helper(node_list)
    return res


for tree in generate_bst(4):
    print(tree)

# Pre-order traversals of binary trees from 1 to n.
# 123
# 132
# 213
# 312
# 321

#   1      1      2      3      3
#    \      \    / \    /      /
#     2      3  1   3  1      2
#      \    /           \    /
#       3  2             2  1
