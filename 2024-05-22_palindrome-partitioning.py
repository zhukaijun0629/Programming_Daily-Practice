'''
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
'''

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        return self.dfs(s, 0, {})

    def dfs(self, s, start_idx, memo):
        if start_idx in memo:
            print('-----READ-----')
            print(start_idx)
            print(memo[start_idx])
            return memo[start_idx]
        if start_idx >= len(s):
            return [[]]
        res = []
        for idx in range(start_idx, len(s)):
            candidate = s[start_idx: idx + 1]
            if self.isPalindrome(candidate):
                following_candidates = self.dfs(s, idx + 1, memo)
                for following_candidate in following_candidates:
                    res.append([candidate] + following_candidate)
        print('-----SAVE-----')
        memo[start_idx] = res
        print(memo)
        return res

    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        return s == s[::-1]


print(Solution().partition('aaabc'))
