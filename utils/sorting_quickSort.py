import random


class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortInteger(self, A):
        if not A:
            return A
        self.quickSort(A, 0, len(A) - 1)
        return A

    def quickSort(self, A, start, end):
        if start >= end:
            return

        # pivot_idx = random.randint(start, end)
        pivot_idx = (start + end) // 2
        pivot = A[pivot_idx]
        left, right = start, end
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        self.quickSort(A, start, right)
        self.quickSort(A, left, end)


print(Solution().sortInteger([11, 12, 13, 14, 4, 5, 6, 7, 8]))
