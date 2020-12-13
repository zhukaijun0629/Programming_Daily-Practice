"""
Hi, here's your problem today. This problem was recently asked by LinkedIn:

Given a string, rearrange the string so that no character next to each other are the same. If no such arrangement is possible, then return None.

Example:
Input: abbccc
Output: cbcbca

Leetcode #767. Reorganize String
"""

def rearrangeString(s):
    # Fill this in.
    a = sorted(sorted(s),key = s.count)
    h = len(a)//2
    a[1::2], a[::2]=a[:h],a[h:]
    return ''.join(a) *  (a[-1:] != a[-2:-1])

print (rearrangeString('abbccc'))
# cbcabc
