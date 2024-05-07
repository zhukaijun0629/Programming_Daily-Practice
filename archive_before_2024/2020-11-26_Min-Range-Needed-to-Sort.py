"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given a list of integers, return the bounds of the minimum range that must be sorted so that the whole list would be sorted.

Example:
Input: [1, 7, 9, 5, 7, 8, 10]
Output: (1, 5)
Explanation:
The numbers between index 1 and 5 are out of order and need to be sorted.
"""

def findRange(nums):
    """Sort the list and check in what range the nums are different"""
    nums_sorted = sorted(nums)
    is_same = [a==b for (a,b) in zip(nums,nums_sorted)]
    try:
        start = is_same.index(False)
        end = len(is_same) - 1 -is_same[::-1].index(False)
        return (start,end)
    except:
        return None





print (findRange([1, 7, 9, 5, 7, 8, 10]))
# (1, 5)
print (findRange([1, 1, 1]))
# None
