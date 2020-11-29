"""
Hi, here's your problem today. This problem was recently asked by Amazon:

Given two arrays, write a function to compute their intersection - the intersection means the numbers that are in both arrays.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:
Each element in the result must be unique.
The result can be in any order.
"""

class Solution:
    def intersection(self, nums1, nums2):
        # Fill this in.
        nums1 = sorted(set(nums1))
        nums2 = sorted(set(nums2))
        if len(nums2)<len(nums1):
            nums1, nums2 = nums2, nums1
        ans = []
        for num in nums1:
            if num in nums2:
                ans.append(num)
        return ans


print (Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))
# [9, 4]
