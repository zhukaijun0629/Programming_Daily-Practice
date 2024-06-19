'''
树的遍历
'''

import collections

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bfs_tree_node(root, result):
    if not root:
        return

    queue = collections.deque([root, 0])
    while queue:
        node, level = queue.popleft()
        # do somethings
        result.append(node.val)
        if node.left:
            queue.append(node.left, level + 1)
        if node.right:
            queue.append(node.right, level + 1)
    return result


def bfs_tree_level(root, result):
    if not root:
        return

    queue = [root]
    level = -1
    while queue:
        level += 1
        next_queue = []
        for node in queue:
            # do somethins with this layer nodes...
            result.append(node.val)
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        queue = next_queue
    return result


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(9)
    tree.right = TreeNode(0)
    tree.left.left = TreeNode(5)
    tree.left.right = TreeNode(1)
    print(bfs_tree_node(tree, []))
    # [4, 9, 0, 5, 1]
