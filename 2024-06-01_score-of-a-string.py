'''
3110. Score of a String

You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the score of s.
'''

class Solution:
    def scoreOfString(self, s: str) -> int:
        if not s:
            return 0

        res = 0
        for i in range(1, len(s)):
            res += abs(ord(s[i])-ord(s[i-1]))

        return res
    

print(Solution().scoreOfString('a'))
print(Solution().scoreOfString('ab'))
print(Solution().scoreOfString('acd'))
print(Solution().scoreOfString('aaaa'))
print(Solution().scoreOfString('aea'))



