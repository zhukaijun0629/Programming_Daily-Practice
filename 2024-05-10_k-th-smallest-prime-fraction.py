'''
786. K-th Smallest Prime Fraction

You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

Constraints:

2 <= arr.length <= 1000
1 <= arr[i] <= 3 * 104
arr[0] == 1
arr[i] is a prime number for i > 0.
All the numbers of arr are unique and sorted in strictly increasing order.
1 <= k <= arr.length * (arr.length - 1) / 2
 

Follow up: Can you solve the problem with better than O(n2) complexity?
'''

from heapq import heappush, heappop
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        minHeap = []
        l, r = 0, len(arr) - 1
        while l < r:
            heappush(minHeap, (arr[l]/arr[-1], l, r))
            l += 1
        while k:
            _, l, r = heappop(minHeap)
            heappush(minHeap, (arr[l]/arr[r-1], l, r-1))
            k -= 1
        return [arr[l], arr[r]]

    def kthSmallestPrimeFraction2(self, arr: List[int], k: int) -> List[int]:
        minHeap = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                heappush(minHeap, (arr[i]/arr[j], [arr[i], arr[j]]))
        while k:
            _, ans = heappop(minHeap)
            k -= 1
        return ans


# [1,2,3,5]  1/5, 1/3, 2/5, 1/2, 3/5, 2/3  
#1/5 2/5 3/5
#2/5 3/5 1/3 + 1/5
#1/2 2/5 3/5 + 1/3

#1/2,1/3,1/5
#1/2,1/3,2/5 + 1/5
#1/2,2/5,2/3 + 1/3 

print(Solution().kthSmallestPrimeFraction([1, 2, 3, 5], 3))
