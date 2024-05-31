'''
260. Single Number III

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Constraints:

2 <= nums.length <= 3 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
Each integer in nums will appear twice, only two integers will appear once.
'''

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        memo = set()
        for num in nums:
            if num in memo:
                memo.remove(num)
            else:
                memo.add(num)
        return list(memo)
    
    
    
### [1,2,2,3,3,4]
print(Solution().singleNumber([1,2,2,3,3,4]))