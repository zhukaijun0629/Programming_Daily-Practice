"""
Hi, here's your problem today. This problem was recently asked by Uber:

Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3 variables a, b, c where a2 + b2 = c2

Example:
Input: [3, 5, 12, 5, 13]
Output: True
Here, 52 + 122 = 132.
"""

def findPythagoreanTriplets(nums):
    for i in range(len(nums)):
        nums[i]**=2
    nums.sort()
    for i in range(len(nums)-1,1,-1):
        j=0
        k=i-1
        while j<k:
            if nums[j]+nums[k]==nums[i]:
                return True
            else:
                if nums[j]+nums[k]<nums[i]:
                    j+=1
                else:
                    k-=1
    return False


print (findPythagoreanTriplets([3, 5, 4, 13]))
# True
