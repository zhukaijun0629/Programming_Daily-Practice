"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

You are given a doubly linked list. Determine if it is a palindrome.

Can you do this for a singly linked list?
"""

class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None

def is_palindrome(node):
    # Fill this in.
    fast = slow = node
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    if not fast:
        first = slow.prev
    else:
        first = slow
    while first and first.val == slow.val:
        first,slow=first.prev,slow.next
    return not first


node = Node('a')
node.next = Node('b')
node.next.prev = node
node.next.next = Node('b')
node.next.next.prev = node.next
node.next.next.next = Node('a')
node.next.next.next.prev = node.next.next

print (is_palindrome(node))
# True
