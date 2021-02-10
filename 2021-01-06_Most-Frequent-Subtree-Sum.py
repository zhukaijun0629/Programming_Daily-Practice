"""
Hi, here's your problem today. This problem was recently asked by LinkedIn:

Given a binary tree, find the most frequent subtree sum.

Example:

   3
  / \
 1   -3

The above tree has 3 subtrees. The root node with 3, and the 2 leaf nodes, which gives us a total of 3 subtree sums. The root node has a sum of 1 (3 + 1 + -3), the left leaf node has a sum of 1, and the right leaf node has a sum of -3. Therefore the most frequent subtree sum is 1.

If there is a tie between the most frequent sum, you can return any one of them.
Leetcode #508
"""
class Node():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def most_freq_subtree_sum(root):
    # fill this in.
    if not root:
        return None

    mp = {}
    def dfs(node):
        if not node:
            return 0
        left_sum = dfs(node.left)
        right_sum = dfs(node.right)
        cur_sum = node.val + left_sum + right_sum
        mp[cur_sum] = mp.get(cur_sum,0) + 1
        return cur_sum

    dfs(root)
    return sorted(mp.items(),key=lambda x: x[1])[-1][0]


root = Node(3, Node(2), Node(-3))
print(most_freq_subtree_sum(root))
# 1
