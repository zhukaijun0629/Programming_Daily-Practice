"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

Given a string, determine if there is a way to arrange the string such that
the string is a palindrome. If such arrangement exists, return a palindrome
(There could be many arrangements). Otherwise return None.
"""

import collections


def find_palindrome(s):
    ct = collections.Counter(s)
    ct = sorted(ct.items(), reverse=True, key=lambda kv: (kv[1] % 2, kv[1]))
    if len(ct) > 1 and ct[1][1] % 2 == 1:
        return None
    res = collections.deque([])
    if ct[0][1] % 2 == 1:
        res.append(ct[0][0])
        ct[0] = (ct[0][0], ct[0][1] - 1)
    for chr, num in ct:
        while num > 0:
            res.append(chr)
            res.appendleft(chr)
            num -= 2
    return "".join(res)


print(find_palindrome('momooom'))
# momom
