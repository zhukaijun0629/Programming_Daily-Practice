"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

Given a binary tree, find the level in the tree where the sum of all nodes on that level is the greatest.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"(Value: {self.value} Left: {self.left} Right: {self.right})"


def tree_level_max_sum(root):
    # Fill this in.
    if not root:
        return 0
    max_level_sum = 0
    queue = [root]
    while queue:
        cur_level_sum = 0
        next_queue = []
        for node in queue:
            cur_level_sum += node.value
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        queue = next_queue
        max_level_sum = max(max_level_sum, cur_level_sum)
    return max_level_sum


n3 = Node(4, Node(3), Node(2))
n2 = Node(5, Node(4), Node(-1))
n1 = Node(1, n2, n3)

"""
    1          Level 0 - Sum: 1
   / \
  4   5        Level 1 - Sum: 9 
 / \ / \
3  2 4 -1      Level 2 - Sum: 8

"""

print(tree_level_max_sum(n1))
# Should print 1 as level 1 has the highest level sum
