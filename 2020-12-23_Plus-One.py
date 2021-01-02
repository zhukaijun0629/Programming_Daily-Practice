"""
Hi, here's your problem today. This problem was recently asked by LinkedIn:

Given a non-empty array where each element represents a digit of a non-negative integer, add one to the integer. The most significant digit is at the front of the array and each element in the array contains only one digit. Furthermore, the integer does not have leading zeros, except in the case of the number '0'.

Example:
Input: [2,3,4]
Output: [2,3,5]

Leetcode #66
"""

class Solution():
  def plusOne(self, digits):
    # Fill this in.
    if len(digits) == 0:
        digits = [1]
    elif digits[-1] == 9:
        digits = self.plusOne(digits[:-1])
        digits += [0]
    else:
        digits[-1] += 1
    return digits

num = [2, 9, 9]
print(Solution().plusOne(num))
# [3, 0, 0]
