'''
3075. Maximize Happiness of Selected Children

You are given an array happiness of length n, and a positive integer k.

There are n children standing in a queue, where the ith child has happiness value happiness[i]. You want to select k children from these n children in k turns.

In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1. Note that the happiness value cannot become negative and gets decremented only if it is positive.

Return the maximum sum of the happiness values of the selected children you can achieve by selecting k children.

Constraints:
1 <= n == happiness.length <= 2 * 105
1 <= happiness[i] <= 108
1 <= k <= n
'''

from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        if not happiness or k <= 0:
            return 0
        happiness.sort()
        maxHappiness = 0
        numberOfSelectedChildren = 0
        while k > 0:
            maxHappiness += max(0, happiness.pop()-numberOfSelectedChildren)
            numberOfSelectedChildren += 1
            k -= 1
        return maxHappiness


# [5,3,6,4,5] after sorting [6,5,5,4,3] select 3 (6-0)+(5-1)+(5-2) sum(max(happiness-#turn,0)) expects 13
print(Solution().maximumHappinessSum([5,3,6,4,5],3))
