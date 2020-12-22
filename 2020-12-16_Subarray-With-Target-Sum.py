"""
Hi, here's your problem today. This problem was recently asked by Amazon:

You are given an array of integers, and an integer K. Return the subarray which sums to K. You can assume that a solution will always exist.
"""

def find_continuous_k(list, k):
    # Fill this in.
    list = [0]+list
    sum = 0
    res=[]
    d = {}
    for i,n in enumerate(list):
        sum += n
        if (sum-k) in d:
            for j in d[sum-k]:
                res.append(list[j+1:i+1])
        d[sum] = d.get(sum,[])+[i]
    return res


print (find_continuous_k([1, 3, 2, 5, 7, 2], 14))
# [2, 5, 7]
