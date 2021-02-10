"""
Hi, here's your problem today. This problem was recently asked by Apple:

You are given a tree, and your job is to print it level-by-level with linebreaks.

    a
   / \
  b   c
 / \ / \
d  e f  g

The output should be
a
bc
defg
"""

from collections import deque

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __str__(self):
    # Fill this in.
    res = ''
    queue = deque([(self,0)])
    cur_level = 0
    cur_level_elements = ''
    while queue:
        element,level = queue.popleft()
        if level > cur_level:
            res += cur_level_elements+('\n')
            cur_level_elements = ''
        cur_level = level
        cur_level_elements += element.val
        if element.left: queue.append((element.left,level+1))
        if element.right: queue.append((element.right,level+1))
    res += cur_level_elements
    return res

tree = Node('a')
tree.left = Node('b')
tree.right = Node('c')
tree.left.left = Node('d')
tree.left.right = Node('e')
tree.right.left = Node('f')
tree.right.right = Node('g')

print (tree)
# a
# bc
# defg
