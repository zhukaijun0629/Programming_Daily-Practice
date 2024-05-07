'''
948. Bag of Tokens
You have an initial power of power, an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

Your goal is to maximize your total score by potentially playing each token in one of two ways:

If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.
Each token may be played at most once and in any order. You do not have to play all the tokens.

Return the largest possible score you can achieve after playing any number of tokens.
'''

from collections import deque
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        res = cur = 0
        tokens.sort()
        queue = deque(tokens)
        
        while queue and (power >= queue[0] or cur):
            if power >= queue[0]:
                power -= queue.popleft()
                cur += 1
            else:
                cur -= 1
                power += queue.pop()
            res = max(res, cur)
        
        return res
                


print(Solution().bagOfTokensScore([100,200,300,400], 200))
                