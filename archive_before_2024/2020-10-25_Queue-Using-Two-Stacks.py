"""
Hi, here's your problem today. This problem was recently asked by Apple:

You are given an array. Each element represents the price of a stock on that particular day. Calculate and return the maximum profit you can make from buying and selling that stock only once.

For example: [9, 11, 8, 5, 7, 10]

Here, the optimal trade is to buy when the price is 5, and sell when it is 10, so the return value should be 5 (profit = 10 - 5 = 5).
"""

class Queue:
    def __init__(self):
        # Fill this in.
        self.queue=[]

    def enqueue(self, val):
        # Fill this in.
        self.queue.append(val)
        # print(self.queue)


    def dequeue(self):
        # Fill this in.
        if self.queue:
            return self.queue.pop(0)
        else:
            return "Index out of range"


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print (q.dequeue())
print (q.dequeue())
print (q.dequeue())
print (q.dequeue())
# 1 2 3
