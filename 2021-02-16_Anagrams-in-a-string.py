"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given 2 strings s and t, find and return all indexes in string s where t is an anagram.
Leetcode #438
"""

from collections import Counter

def find_anagrams(s, t):
    # Fill this in.
    res = []
    counter_t = Counter(t)
    counter_s = Counter(s[:len(t) - 1])
    for i in range(len(t) - 1, len(s)):
        counter_s[s[i]] += 1
        start_idx = i - len(t) + 1
        if counter_s == counter_t:
            res.append(start_idx)
        counter_s[s[start_idx]] -= 1
        if not counter_s[s[start_idx]]:
            del counter_s[s[start_idx]]
    return res

def getAnagrams(s):
    if not s:
        return []
    
    visited = [0] * len(s)
    anagrams = []

    def dfs(s, visited, candidate, anagrams):
        if len(s) == len(candidate):
            anagrams.append(''.join(candidate))
            return
        for i in range(len(s)):
            if visited[i]:
                continue
            if i > 0 and s[i-1] == s[i] and not visited[i-1]:
                continue
            visited[i] = True
            candidate.append(s[i])
            dfs(s, visited, candidate, anagrams)
            visited[i] = False
            candidate.pop()

    dfs(sorted(s), visited, [], anagrams)
    return anagrams


print(find_anagrams('acdbacdacb', 'abc'))
# [3, 7]
