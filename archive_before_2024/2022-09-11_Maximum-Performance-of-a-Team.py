'''
1383. Maximum Performance of a Team
You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.

Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.

Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 109 + 7.
'''
import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        result = 0
        s_sum = 0
        e_min_heap = []
        for e, s in sorted(zip(efficiency,speed), reverse=1):
            heapq.heappush(e_min_heap, s)
            s_sum += s
            if len(e_min_heap) > k:
                s_sum -= heapq.heappop(e_min_heap)
            result = max(result, e*s_sum)

        return result % (10**9 + 7)


print(Solution().maxPerformance(6,
[2,10,3,1,5,8],
[5,4,3,9,7,2],
2))