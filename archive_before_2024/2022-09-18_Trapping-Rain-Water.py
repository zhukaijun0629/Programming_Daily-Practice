'''
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

'''

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        max_ht = max(height)
        max_ht_idx = height.index(max_ht)

        def trap_to_max(height):
            cur_max = 0
            trapped = 0
            for ht in height:
                if ht < cur_max:
                    trapped += cur_max - ht
                else:
                    cur_max = ht
            return trapped
        
        return trap_to_max(height[:max_ht_idx]) + trap_to_max(reversed(height[max_ht_idx+1:]))

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))