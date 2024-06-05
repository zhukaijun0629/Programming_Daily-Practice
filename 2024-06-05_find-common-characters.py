'''
1002. Find Common Characters

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
'''

from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []
        
        char_counts = Counter(words[0])
        
        for word in words[1:]:
            char_counts &= Counter(word)
            
        results = []
        for char, count in char_counts.items():
            results.extend([char] * count)
            
        return results

print(Solution().commonChars(['bella','label','roller']))
print(Solution().commonChars(['cool','lock','cook']))
print(Solution().commonChars(['']))
print(Solution().commonChars([]))
print(Solution().commonChars(['aaa','bbb']))
print(Solution().commonChars(['aaa','bbbaaa']))

