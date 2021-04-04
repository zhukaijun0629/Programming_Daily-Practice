"""
Hi, here's your problem today. This problem was recently asked by Apple:

Create a class that initializes with a list of numbers and has one method called sum. sum should take in two parameters, start_idx and end_idx and return the sum of the list from start_idx (inclusive) to end_idx` (exclusive).

You should optimize for the sum method.
"""


class ListFastSum:
    def __init__(self, nums):
        self.nums = nums

    def sum(self, start_idx, end_idx):
        # Fill this in.
        sum_sofar = [0] * (len(self.nums)+1)
        sum_sofar[1] = self.nums[0]
        for i in range(2, len(self.nums)+1):
            sum_sofar[i] = sum_sofar[i-1] + self.nums[i-1]
        return sum_sofar[end_idx] - sum_sofar[start_idx]



print(ListFastSum([1, 2, 3, 4, 5, 6, 7]).sum(2, 5))
# 12 because 3 + 4 + 5 = 12
