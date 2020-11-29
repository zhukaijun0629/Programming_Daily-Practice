"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution:

  def addTwoNumbers(self, l1, l2, c = 0):
    # Fill this in.

    if not l1 and not l2:
        return

    # l3=dummy=ListNode((l1.val+l2.val+c)%10)
    # c=(l1.val+l2.val)//10
    # l1=l1.next
    # l2=l2.next
    # dummy.next=self.addTwoNumbers(l1, l2, c)
    # return l3

    l3=ListNode((l1.val+l2.val+c)%10)
    l3.next=self.addTwoNumbers(l1.next, l2.next, (l1.val+l2.val)//10)
    return l3


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val)
  result = result.next
# 7 0 8
