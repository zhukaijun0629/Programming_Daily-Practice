'''
1208. Get Equal Substrings Within Budget

You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.

Constraints:

1 <= s.length <= 105
t.length == s.length
0 <= maxCost <= 106
s and t consist of only lowercase English letters.
'''


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i = 0
        for j in range(len(s)):
            cost_j = abs(ord(s[j])-ord(t[j]))
            maxCost -= cost_j
            if maxCost < 0:
                cost_i = abs(ord(s[i])-ord(t[i]))
                maxCost += cost_i
                i += 1
        return j-i+1

    def equalSubstring2(self, s: str, t: str, maxCost: int) -> int:
        i = 0
        res = 0
        for j in range(len(s)):
            cost_j = abs(ord(s[j])-ord(t[j]))
            maxCost -= cost_j
            while maxCost < 0:
                cost_i = abs(ord(s[i])-ord(t[i]))
                maxCost += cost_i
                i += 1
            res = max(res, j-i+1)
        return res


'''
1,2,3,1,1  maxCost=5
4
2
-1
'''
print(Solution().equalSubstring('abc', 'bcd', 2))
print(Solution().equalSubstring('aaaaa', 'bcdbb', 5))

print(Solution().equalSubstring2('abc', 'bcd', 2))
print(Solution().equalSubstring2('aaaaa', 'bcdbb', 5))
