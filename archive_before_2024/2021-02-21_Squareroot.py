"""
Hi, here's your problem today. This problem was recently asked by Google:

Given a positive integer, find the square root of the integer without using any built in square root or power functions (math.sqrt or the ** operator). Give accuracy up to 3 decimal points.
"""


def sqrt(x):
    # Fill this in.
    lo = 0
    hi = x
    while lo + 0.001 < hi:
        mid = (lo + hi) / 2
        if mid * mid > x:
            hi = mid
        else:
            lo = mid
    if abs(lo * lo - x) < abs(hi * hi -x):
        return round(lo, 3)
    else:
        return round(hi, 3)

print(sqrt(5))
# 2.236
