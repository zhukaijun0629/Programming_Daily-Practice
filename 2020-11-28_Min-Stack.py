"""
Hi, here's your problem today. This problem was recently asked by Uber:

Design a simple stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Note: be sure that pop() and top() handle being called on an empty stack.

Leetcode #155
"""

class minStack(object):

    def __init__(self):
        # Fill this in.
        self.stack = []


    def push(self, x):
        if not self.stack:
            self.stack.append((x,x))
        else:
            self.stack.append((x,min(x,self.stack[-1][1])))


    def pop(self):
        # Fill this in.
        if self.stack:
            self.stack.pop()

    def top(self):
        # Fill this in.
        if self.stack:
            return self.stack[-1][0]

    def getMin(self):
        # Fill this in.
        if self.stack:
            return self.stack[-1][1]

x = minStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
# -3
x.pop()
print(x.top())
# 0
print(x.getMin())
# -2
