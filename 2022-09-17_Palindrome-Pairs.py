'''
336. Palindrome Pairs

Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.
'''

from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            return word == word[::-1]
        
        words:dict = {word: idx for idx, word in enumerate(words)}
        valid_pals = []
        for word, i in words.items():
            n = len(word)
            for j in range(n+1):
                prefix = word[:j]
                suffix = word[j:]
                if is_palindrome(prefix):
                    target = suffix[::-1]
                    if target != word and target in words:
                        valid_pals.append([words[target], i])
                if j != n and is_palindrome(suffix):
                    target = prefix[::-1]
                    if target != word and target in words:
                        valid_pals.append([i, words[target]])

        return valid_pals

print(Solution().palindromePairs(["abcd","dcba","lls","s","sssll"]))