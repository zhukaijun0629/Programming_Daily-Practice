"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given a string with the initial condition of dominoes, where:

. represents that the domino is standing still
L represents that the domino is falling to the left side
R represents that the domino is falling to the right side

Figure out the final position of the dominoes. If there are dominoes that get pushed on both ends, the force cancels out and that domino remains upright.

Example:
Input:  ..R...L..R.
Output: ..RR.LL..RR
"""

class Solution(object):
    def pushDominoes(self, dominoes):
        d = 'L' + dominoes + 'R'
        res = ""
        i = 0
        for j in range(1, len(d)):
            if d[j] == '.':
                continue               #Move right pointer to the next letter
            middle = j - i - 1         #Count number of dots in between left and right pointers
            if i:
                res += d[i]                         #Add left pointer letter, except for the very first 'L'
            if d[i] == d[j]:
                res += d[i] * middle                #If left pointer and right pointer have the same letter, then the dots in between will fall to the same letter
            elif d[i] == 'L' and d[j] == 'R':
                res += '.' * middle                 #If left pointer is L and right pointer is R, then the dots in between remain dots
            else:
                res += 'R' * (middle // 2) + '.' * (middle % 2) + 'L' * (middle // 2)  #If left pointer is R and right pointer is L, then the dots in between will fall half and half
            i = j
        return res



print (Solution().pushDominoes('..R...L..R.'))
# ..RR.LL..RR
print (Solution().pushDominoes('R.R.L'))
