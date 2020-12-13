"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given an array of characters with repeats, compress it in place. The length after compression should be less than or equal to the original array.

Example:
Input: ['a', 'a', 'b', 'c', 'c', 'c']
Output: ['a', '2', 'b', 'c', '3']
"""

class Solution(object):
    def compress(self, chars):
        # Fill this in.
        i = 0
        num = 0
        for c in chars:
            if c != chars[i]:
                if num == 1:
                    chars[i+1] = c
                    i += 1
                else:
                    for digit in str(num):
                        chars[i+1] = digit
                        i += 1
                    num = 1
                    chars[i+1] = c
                    i += 1
            else:
                num += 1
        if num > 1:
            for digit in str(num):
                chars[i+1] = digit
                i += 1
        return chars[:i+1]


print (Solution().compress(['a', 'a', 'b', 'c', 'c', 'c']))
# ['a', '2', 'b', 'c', '3']
print (Solution().compress(['a', 'b', 'c', 'c', 'c']))
# ['a', 'b', 'c', '3']
print (Solution().compress(['a', 'b', 'c']))
# ['a', 'b', 'c']
