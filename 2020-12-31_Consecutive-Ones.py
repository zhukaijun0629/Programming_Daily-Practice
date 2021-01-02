"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

Return the longest run of 1s for a given integer n's binary representation.

Example:
Input: 242
Output: 4
242 in binary is 0b11110010, so the longest run of 1 is 4.
"""

def longest_run(n):
    # Fill this in.
    res = 0
    cur = 0
    while n > 0:
        if n % 2 == 1:
            cur += 1
        else:
            res = max(res, cur)
            cur = 0
        n = n//2
    return max(res, cur)

print (longest_run(242))
# 4
