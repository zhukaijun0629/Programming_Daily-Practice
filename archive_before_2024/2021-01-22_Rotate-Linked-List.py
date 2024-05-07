"""
Hi, here's your problem today. This problem was recently asked by AirBNB:

Given a linked list and a number k, rotate the linked list by k places.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        current = self
        ret = ''
        while current:
            ret += str(current.value)
            current = current.next
        return ret


def rotate_list(list, k):
    # Fill this in.
    length = 0
    pre = end = Node(-1)
    pre.next = end.next = list
    while end.next:
        length += 1
        end = end.next

    if length == 0 or k % length == 0:
        return list

    k = length - k % length

    while k > 0:
        pre = pre.next
        k -= 1
    res = pre.next
    end.next = list
    pre.next = None
    return res


    # Order is 1, 2, 3, 4
llist = Node(1, Node(2, Node(3, Node(4))))

# Order should now be 3, 4, 1, 2
print(rotate_list(llist, 5))
# 3412
