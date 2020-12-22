"""
Hi, here's your problem today. This problem was recently asked by Amazon:

You are given an array of integers. Return the length of the longest consecutive elements sequence in the array.

For example, the input array [100, 4, 200, 1, 3, 2] has the longest consecutive sequence 1, 2, 3, 4, and thus, you should return its length, 4
"""

def longest_consecutive(nums):
    # Fill this in.
    nums.sort()
    mx_len = 0
    cur_stack = []
    for n in nums:
        if not cur_stack or n == cur_stack[-1]+1:
            cur_stack.append(n)
        else:
            if n == cur_stack[-1]: continue
            mx_len = max(mx_len,len(cur_stack))
            cur_stack=[n]
    return max(mx_len,len(cur_stack))

# print (longest_consecutive([100, 4, 200, 1, 3, 2]))
# 4
print (longest_consecutive([0,3,7,2,5,8,4,6,0,1]))
# 9
