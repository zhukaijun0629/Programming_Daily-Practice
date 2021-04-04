"""
Hi, here's your problem today. This problem was recently asked by Apple:

Given 2 binary trees t and s, find if s has an equal subtree in t, where the structure and the values are the same. Return True if it exists, otherwise return False.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"(Value: {self.value} Left: {self.left} Right: {self.right})"


def find_subtree(s, t):
    # Fill this in.
    if not s:
        return True

    s_root = s

    def dfs(t_node):
        if not t_node:
            return False
        if check(s_root, t_node):
            return True
        if check(s_root, t_node.left):
            return True
        if check(s_root, t_node.right):
            return True
        return False
    
    def check(s_node, t_node):
        if not s_node:
            return True
        if s_node.value != t_node.value:
            return False
        if not check(s_node.left, t_node.left):
            return False
        if not check(s_node.right, t_node.right):
            return False
        return True
    return dfs(t)


t2 = Node(4, Node(3), Node(2))
t3 = Node(5, Node(4), Node(-1))
t = Node(1, t2, t3)

s = Node(1, Node(4), Node(5))
"""
Tree t:
    1
   / \
  4   5 
 / \ / \
3  2 4 -1

Tree s:
  4 
 / \
3  2 
"""

print(find_subtree(s, t))
# True
