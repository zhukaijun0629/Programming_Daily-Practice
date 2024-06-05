'''
409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
'''

class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_set = set()
        res = 0
        for c in s:
            if c in letter_set:
                res += 2
                letter_set.remove(c)
            else:
                letter_set.add(c)
                
        if letter_set:
            res += 1
            
        return res

### abcdeeE -> eEe    
print(Solution().longestPalindrome('abcdeeE'))