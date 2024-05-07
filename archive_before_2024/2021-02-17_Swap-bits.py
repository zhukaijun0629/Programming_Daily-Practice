"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given a 32-bit integer, swap the 1st and 2nd bit, 3rd and 4th bit, up til the 31st and 32nd bit.
Leetcode #476
"""


def swap_bits(num):
    # Fill this in.
    i = 1
    while i <= num:
        i = i << 1
    return (i - 1) ^ num


print(f"0b{swap_bits(0b10101010101010101010101010101010):032b}")
# 0b01010101010101010101010101010101
