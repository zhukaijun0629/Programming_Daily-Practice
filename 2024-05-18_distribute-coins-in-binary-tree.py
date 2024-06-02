'''
979. Distribute Coins in Binary Tree

You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.
'''

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def helper(cur_node, parent):
            if cur_node == None:
                return 0

            moves = helper(cur_node.left, cur_node) + \
                helper(cur_node.right, cur_node)
            leftover = cur_node.val - 1
            parent.val += leftover
            moves += abs(leftover)
            return moves

        return helper(root, TreeNode())
