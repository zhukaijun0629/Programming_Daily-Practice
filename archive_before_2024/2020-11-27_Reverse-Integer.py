"""
Hi, here's your problem today. This problem was recently asked by LinkedIn:

Write a function that reverses the digits a 32-bit signed integer, x. Assume that the environment can only store integers within the 32-bit signed integer range, [-2^31, 2^31 - 1]. The function returns 0 when the reversed integer overflows.

Example:
Input: 123
Output: 321

Leetcode #7
"""

class Solution:
    def reverse(self, x):
        # Fill this in.
        sign = [1,-1][x < 0]
        reverse = sign * int(str(abs(x))[::-1])
        return reverse if -(2**31)-1 < reverse < 2**31 else 0

print(Solution().reverse(123))
# 321
print(Solution().reverse(2**31))
# 0
