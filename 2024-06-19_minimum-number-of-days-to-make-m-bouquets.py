'''
1482. Minimum Number of Days to Make m Bouquets

You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

Constraints:

bloomDay.length == n
1 <= n <= 105
1 <= bloomDay[i] <= 109
1 <= m <= 106
1 <= k <= n
'''

from typing import List

class Solution:
    def minDays(self, bloomDays: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDays): return -1

        left, right = 1, max(bloomDays)
        while left < right:
            mid = (left + right) // 2
            cur_bouq = 0
            num_bouq = 0
            for day in bloomDays:
                cur_bouq += 1 if day <= mid else 0
                if cur_bouq == k:
                    num_bouq += 1
                    cur_bouq = 0
                if num_bouq == m: break
            if num_bouq == m:
                right = mid
            else:
                left = mid + 1
        return left
                

