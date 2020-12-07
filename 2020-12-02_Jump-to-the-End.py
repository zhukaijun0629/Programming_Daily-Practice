"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Starting at index 0, for an element n at index i, you are allowed to jump at most n indexes ahead. Given a list of numbers, find the minimum number of jumps to reach the end of the list.

Example:
Input: [3, 2, 5, 1, 1, 9, 3, 4]
Output: 2
Explanation:

The minimum number of jumps to get to the end of the list is 2:
3 -> 5 -> 4
"""

# def jumpToEnd(nums):
#     # Fill this in.
#     hash = [len(nums)]*len(nums)
#     hash[0]=0
#     for i,num in enumerate(nums):
#         for j in range(i+1,min(i+num+1,len(nums))):
#             hash[j]=min(hash[i]+1,hash[j])
#             print(hash)
#     return hash[-1]

def jumpToEnd(nums):
    if len(nums) <= 1: return 0
    l, r = 0, nums[0]
    times = 1
    while r < len(nums) - 1:
        times += 1
        nxt = max(i + nums[i] for i in range(l, r + 1))
        l, r = r + 1, nxt
    return times




print (jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4]))
# 2
