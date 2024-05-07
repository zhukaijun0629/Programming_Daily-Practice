'''
2816. Double a Number Represented as a Linked List

You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.

Constraints:

The number of nodes in the list is in the range [1, 104]
0 <= Node.val <= 9
The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tens_place_value = self.helper(head)
        if tens_place_value:
            head = ListNode(tens_place_value, head) 
        return head
    
    def helper(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        new_total_value = head.val * 2 + self.helper(head.next)
        ones_place_value = new_total_value % 10
        tens_place_value = new_total_value // 10
        head.val = ones_place_value
        return tens_place_value
        
    
    
# 1-> 8->9; 2 1&6 1&8 ; 3->7->8
l1 = ListNode(1, ListNode(8, ListNode(9)))
result = Solution().doubleIt(l1)
while result:
    print(result.val)
    result = result.next
    
# 9->9->9; 1&8 1&8 1&8 ; 1->9->9->8
l2 = ListNode(9,ListNode(9,ListNode(9)))
result = Solution().doubleIt(l2)
while result:
    print(result.val)
    result = result.next
