"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Given an expression (as a list) in reverse polish notation, evaluate
the expression. Reverse polish notation is where the numbers come before
the operand. Note that there can be the 4 operands '+', '-', '*', '/'.
You can also assume the expression will be well formed.

Example
Input: [1, 2, 3, '+', 2, '*', '-']
Output: -9
The equivalent expression of the above reverse polish notation would be
(1 - ((2 + 3) * 2)).
"""


def reverse_polish_notation(expr):
    def calc(a, b, symbol):
        if symbol == "+":
            return a + b
        if symbol == "-":
            return a - b
        if symbol == "*":
            return a * b
        if symbol == "/":
            return a / b

    stack = []
    for c in expr:
        if str(c) not in "+-*/":
            stack.append(c)
            continue
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(calc(num1, num2, c))
    return stack[0] if len(stack) == 1 else None

# 1 - (2 + 3) * 2
print(reverse_polish_notation([1, 2, 3, '+', 2, '*', '-']))
# -9
