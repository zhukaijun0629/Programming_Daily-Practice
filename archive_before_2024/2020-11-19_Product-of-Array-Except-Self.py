"""
Hi, here's your problem today. This problem was recently asked by Amazon:

You are given an array of integers. Return an array of the same size where the element at each index is the product of all the elements in the original array except for the element at that index.

For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 30, 24].

You cannot use division in this problem.
"""

def products(nums):
    # Fill this in.
    if not nums:
        return []
    product = 1
    for num in nums:
        product *= num
    res = []
    for num in nums:
        try:
            res.append(product//num)
        except:
            res.append('Error')
    return res

print (products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]
