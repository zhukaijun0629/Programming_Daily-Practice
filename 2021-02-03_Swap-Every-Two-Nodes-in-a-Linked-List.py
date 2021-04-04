"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given a linked list, swap the position of the 1st and 2nd node, then swap the position of the 3rd and 4th node etc.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value}, ({self.next.__repr__()})"


def swap_every_two(llist, k = 2):
    # Fill this in.
    dummy = jump = Node(0)
    dummy.next = l = r = llist
    while True:
        count = 0
        while r and count < k:
            count += 1
            r = r.next
        if count == k:
            cur = l
            pre = r
            for _ in range(k):
                cur.next, cur, pre = pre, cur.next, cur
            jump.next, l, jump = pre, r, l

        else:
            return dummy.next




llist = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(swap_every_two(llist))
# 2, (1, (4, (3, (5, (None)))))
