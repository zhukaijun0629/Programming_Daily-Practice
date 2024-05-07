"""
Hi, here's your problem today. This problem was recently asked by AirBNB:

The power function calculates x raised to the nth power. If implemented in O(n) it would simply be a for loop over n and multiply x n times. Instead implement this power function in O(log n) time. You can assume that n will be a non-negative integer.
"""
def pow(x, n):
    # Fill this in.
    if n == 0:
        return 1
    if n == 1:
        return x
    if n % 2:
        return x * pow(x, n // 2) ** 2
    else:
        return pow(x, n // 2) ** 2


print(pow(5, 3))
# 125