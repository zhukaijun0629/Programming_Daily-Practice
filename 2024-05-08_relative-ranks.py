'''
506. Relative Ranks

You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

Constraints:

n == score.length
1 <= n <= 104
0 <= score[i] <= 106
All the values in score are unique.
'''

from typing import List
from heapq import heappop, heappush

class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        if not scores:
            return []
        maxHeap = []
        for idx in range(len(scores)):
            heappush(maxHeap,(-scores[idx], idx))
        rank = 1
        cur_score = maxHeap[0][0]
        number_of_same_score = 0
        while maxHeap:
            score, idx = heappop(maxHeap)
            if score > cur_score:
                rank += number_of_same_score
                number_of_same_score = 1
                cur_score = score
            else:
                number_of_same_score += 1
            scores[idx] = self.polishUpRank(rank)
        return scores

    def polishUpRank(self, rank: int) -> str:
        match rank:
            case 1:
                return "Gold Medal"
            case 2:
                return "Silver Medal"
            case 3:
                return "Bronze Medal"
            case _:
                return str(rank)
           

### [5,4,19,3,20] [(5,0)] 
print(Solution().findRelativeRanks([5,4,19,3,20]))
print(Solution().findRelativeRanks([5,5]))
print(Solution().findRelativeRanks([5,5,5]))
print(Solution().findRelativeRanks([5]))
print(Solution().findRelativeRanks([]))
print(Solution().findRelativeRanks([5,5,5,5]))
print(Solution().findRelativeRanks([5,5,3,5]))
print(Solution().findRelativeRanks([5,4,3,4]))
print(Solution().findRelativeRanks([5,3,4,3,3,3,3]))



