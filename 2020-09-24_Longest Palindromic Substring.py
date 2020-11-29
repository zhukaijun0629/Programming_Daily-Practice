"""
Hi, here's your problem today. This problem was recently asked by Twitter:

A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, find the longest palindromic substring in s.

Example:
Input: "banana"
Output: "anana"

Input: "million"
Output: "illi"
"""

class Solution:
    def longestPalindrome(self, s):
      # Fill this in.
        res=''
        for i in range(len(s)):
            temp =self.helper(s,i,i)
            if len(temp)>len(res):
                res=temp
            temp =self.helper(s,i,i+1)
            if len(temp)>len(res):
                res=temp
        return res

    def helper(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]


# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
