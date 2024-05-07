"""
Hi, here's your problem today. This problem was recently asked by Facebook:

You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.

Example:
Given [4, 7, 1 , -3, 2] and k = 5,
return true since 4 + 1 = 5.
"""

def two_sum(list, k):
    dict={}
    for i in range(len(list)):
        if k-list[i] in dict:
            return True
        else:
            dict[list[i]] = i
    return False


print(two_sum([4,2,8,-2,2], 5))
