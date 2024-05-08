class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortInteger(self, A):
        if not A:
            return A
        temp = [0] * len(A)
        self.mergeSort(A, 0, len(A) - 1, temp)
        return A

    def mergeSort(self, A, start, end, temp):
        if start >= end:
            return

        self.mergeSort(A, start, (start + end) // 2, temp)  # mergeSort left
        self.mergeSort(A, (start + end) // 2 + 1, end, temp) # mergeSort right
        self.merge(A, start, end, temp) # merge left and right

    def merge(self, A, start, end, temp):
        mid = (start + end) // 2
        left = start
        right = mid + 1
        idx = start

        while left <= mid and right <= end:
            if A[left] <= A[right]:
                temp[idx] = A[left]
                idx += 1
                left += 1
            else:
                temp[idx] = A[right]
                idx += 1
                right += 1
        while left <= mid:
            temp[idx] = A[left]
            idx += 1
            left += 1
        while right <= end:
            temp[idx] = A[right]
            idx += 1
            right += 1
        for i in range(start, end + 1):
            A[i] = temp[i]


print(Solution().sortInteger([10, 3, 7, 1, 4, 5, 2, 0, 8]))
