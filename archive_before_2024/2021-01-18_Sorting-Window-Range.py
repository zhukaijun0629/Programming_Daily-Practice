"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given a list of numbers, find the smallest window to sort such that the whole
list will be sorted. If the list is already sorted return (0, 0). You can
assume there will be no duplicate numbers.

Example:
Input: [2, 4, 7, 5, 6, 8, 9]
Output: (2, 4)
Explanation: Sorting the window (2, 4) which is [7, 5, 6] will also means that
the whole list is sorted.
"""


def min_window_to_sort(nums):
    left_pt = right_pt = 0
    max_so_far = float('-inf')
    min_so_far = float('inf')
    for i in range(len(nums)):
        if nums[i] > max_so_far:
            max_so_far = nums[i]
        else:
            right_pt = i

        if nums[-i - 1] < min_so_far:
            min_so_far = nums[-i - 1]
        else:
            left_pt = len(nums) - i - 1
    return (left_pt, right_pt)


print(min_window_to_sort([1, 2, 3, 5, 6, 8, 9]))
# (2, 4)
