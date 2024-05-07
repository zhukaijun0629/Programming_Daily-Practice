"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

You are given an array of integers. Return the largest product that can be made by multiplying any 3 integers in the array.

Example:

[-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.
"""

def maximum_product_of_three(lst):
    lst.sort()
    return lst[-1]*max(lst[0]*lst[1],lst[-3]*lst[-2])

print (maximum_product_of_three([-4, -4, 2, 8]))
# 128
print (maximum_product_of_three([-4,5,3,2,12,-3,124, -4, 2, 8]))
