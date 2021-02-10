"""
Hi, here's your problem today. This problem was recently asked by Amazon:

Given a string, return the first recurring letter that appears.
If there are no recurring letters, return None.

Example:
Input: qwertty
Output: t

Input: qwerty
Output: None
"""


def first_recurring_char(s):
    if len(s) <= 1:
        return None
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            return s[i]
    return None


print(first_recurring_char('qwertty'))
# t

print(first_recurring_char('qwerty'))
# None
