"""
Hi, here's your problem today. This problem was recently asked by Amazon:

MS Excel column titles have the following pattern: A, B, C, ..., Z, AA, AB, ..., AZ, BA, BB, ..., ZZ, AAA, AAB, ... etc. In other words, column 1 is named "A", column 2 is "B", column 26 is "Z", column 27 is "AA" and so forth. Given a positive integer, find its corresponding column name.
Examples:
Input: 26
Output: Z

Input: 51
Output: AY

Input: 52
Output: AZ

Input: 676
Output: YZ

Input: 702
Output: ZZ

Input: 704
Output: AAB

Leetcode #168
"""

class Solution:
    def convertToTitle(self, n):
        # Fill this in.
        # return "" if n == 0 else self.convertToTitle((n-1)//26) + chr((n-1)%26+ord('A'))
        res = ''
        while (n-1)/26 >= 1:
            res = chr(65 + (n-1) % 26) + res
            n = (n-1)//26
        res = chr(65 + (n-1) % 26) + res
        return res
input1 = 1
input2 = 456976
input3 = 28
print(Solution().convertToTitle(input1))
# A
print(Solution().convertToTitle(input2))
# YYYZ
print(Solution().convertToTitle(input3))
# AB
