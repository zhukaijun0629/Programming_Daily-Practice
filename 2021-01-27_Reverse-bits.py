"""
Hi, here's your problem today. This problem was recently asked by Amazon:

Given a 32 bit integer, reverse the bits and return that number.

Example:
Input: 1234
# In bits this would be 0000 0000 0000 0000 0000 0100 1101 0010
Output: 1260388352
# Reversed bits is 0100 1011 0010 0000 0000 0000 0000 0000
"""


def to_bits(n):
    return f'{n:08b}'


def reverse_num_bits(num):
    ans = 0
    for _ in range(32):
        ans = ans << 1 | (num & 1)
        num >>= 1
    return ans


print(to_bits(1234))
# 10011010010
print(reverse_num_bits(1234))
# 1260388352
print(to_bits(reverse_num_bits(1234)))
# 1001011001000000000000000000000
