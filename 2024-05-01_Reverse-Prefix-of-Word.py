"""
2000. Reverse Prefix of Word

Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
Return the resulting string.

Constraints:

1 <= word.length <= 250
word consists of lowercase English letters.
ch is a lowercase English letter.
"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        ch_index = word.index(ch)
        return word[ch_index::-1] + word[ch_index+1:]


print(Solution().reversePrefix("abcdabc", "d"))
### expect "dcbaabc"

print(Solution().reversePrefix("abcdabc", "z"))
### expect "abcdabc"

print(Solution().reversePrefix("abcdabcd", "d"))
### expect "dcbaabcd"
