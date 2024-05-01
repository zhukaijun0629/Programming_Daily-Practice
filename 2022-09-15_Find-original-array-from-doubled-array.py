'''
2007. Find Original Array From Doubled Array

An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.
'''

from collections import Counter
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort(reverse = 1)
        double = Counter()
        single = []
        for num in changed:
            if 2 * num not in double:
                double[num] += 1
            else:
                double[2*num] -= 1
                if double[2*num] == 0:
                    del double[2*num]
                single.append(num)
        
        if len(single) == len(changed)/2:
            return single
        else:
            return []


# expect [1,2,2]
print(Solution().findOriginalArray([2,1,2,4,2,4]))