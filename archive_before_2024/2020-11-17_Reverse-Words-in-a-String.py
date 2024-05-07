"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "The cat in the hat"
Output: "ehT tac ni eht tah"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""

class Solution:
    def reverseWords(self, str):
        # Fill this in.
        tmp = str.split(" ")
        tmp = [x[::-1] for x in tmp]
        return ' '.join(tmp)

print (Solution().reverseWords("The cat in the hat"))
# ehT tac ni eht tah
