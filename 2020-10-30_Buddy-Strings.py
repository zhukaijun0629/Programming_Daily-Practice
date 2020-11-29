"""
Hi, here's your problem today. This problem was recently asked by AirBNB:

Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

Example 1:
Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:
Input: A = "aa", B = "aa"
Output: true
Example 4:
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:
Input: A = "", B = "aa"
Output: false
"""

class Solution:
    def buddyStrings(self, A, B):
        # Fill this in.
        if len(A)!=len(B) or (A==B and len(A)==len(set(A))):
            return False
        stackA , stackB = [] , []
        for i in range(len(A)):
            if A[i] != B[i]:
                stackA.append(A[i])
                stackB.append(B[i])
            if len(stackA)>2:
                return False

        if not stackA:
            return True
        if len(stackA)==2 and sorted(stackA)==sorted(stackB):
            return True

print (Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print (Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False
