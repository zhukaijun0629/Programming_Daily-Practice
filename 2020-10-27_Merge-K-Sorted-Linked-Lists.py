"""
Hi, here's your problem today. This problem was recently asked by Twitter:

You are given an array of k sorted singly linked lists. Merge the linked lists into a single sorted linked list and return it.
"""

class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer

def mergeTwoLists(l1, l2):
    l3=dummy=Node(0)
    while l1 and l2:
        if l1.val<=l2.val:
            l3.next=l1
            l1=l1.next
            l3=l3.next
        else:
            l3.next=l2
            l2=l2.next
            l3=l3.next
    else:
        l3.next=l1 or l2
    return dummy.next

def merge(lists):
    amount=len(lists)
    interval = 1
    while interval < amount:
        for i in range(0,amount-interval,interval*2):
            lists[i]=mergeTwoLists(lists[i],lists[i+interval])
        interval*=2
    return lists[0] if amount>0 else None




a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print (merge([a, b]))
# 123456
