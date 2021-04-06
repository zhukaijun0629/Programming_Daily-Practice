"""
Hi, here's your problem today. This problem was recently asked by Amazon:

Given a sorted linked list of integers, remove all the duplicate elements in the linked list so that all elements in the linked list are unique.

Leetcode #83
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"({self.value}, {self.next})"


def remove_dup(lst):
    # Fill this in.
    dummy = Node(-1)
    pre = dummy
    pre.next = tail = lst
    while tail:
        if tail.next and tail.next.value == tail.value:
            tail = tail.next
        else:
            pre.next = tail
            pre = tail
            tail = pre.next
    return dummy.next


lst = Node(1, Node(2, Node(2, Node(3, Node(3, Node(3))))))

remove_dup(lst)
print(lst)
# (1, (2, (3, None)))
