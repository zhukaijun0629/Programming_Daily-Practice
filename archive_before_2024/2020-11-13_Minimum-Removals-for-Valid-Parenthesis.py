"""
Hi, here's your problem today. This problem was recently asked by Uber:

You are given a string of parenthesis. Return the minimum number of parenthesis that would need to be removed in order to make the string valid. "Valid" means that each open parenthesis has a matching closed parenthesis.

Example:

"()())()"

The following input should return 1.

")("
"""


def count_invalid_parenthesis(string):
    # Fill this in.
    ans = ''
    stack = []
    for c in string:
        if c == "(":
            stack.append(c)
        if c == ")":
            if stack:
                stack.pop()
            else:
                ans+=c
    while stack:
        ans=stack.pop()+ans
    return len(ans)


print (count_invalid_parenthesis("()(()"))
# 1
