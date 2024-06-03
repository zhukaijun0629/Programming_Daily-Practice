
def sortIntegerQuick(nums):
	if not nums:
		return []
	quickSort(nums, 0, len(nums) - 1)
	return nums

def quickSort(nums, start, end):
	if start >= end:
		return
	
	pivot_idx = (start + end) // 2
	pivot = nums[pivot_idx]

	left = start
	right = end
	while left <= right:
		while left <= right and nums[left] < pivot:
			left += 1
		while left <= right and nums[right] > pivot:
			right -= 1
		if left <= right:
			nums[left], nums[right] = nums[right], nums[left]
			left +=1
			right -= 1
	quickSort(nums, start, right)
	quickSort(nums, left, end)


def sortIntegerMerge(nums):
	if not nums:
		return []
	temp = [0] * len(nums)
	mergeSort(nums, 0, len(nums) - 1, temp)
	return nums

def mergeSort(nums, start, end, temp):
	if start >= end:
		return
	
	mergeSort(nums, start, (start + end) // 2, temp)
	mergeSort(nums, (start + end) // 2 + 1, end, temp)
	merge(nums, start, end, temp)

def merge(nums, start, end, temp):
	idx = start
	mid = (start + end) // 2
	left = start
	right = mid + 1

	while left <= mid and right <= end:
		if nums[left] < nums[right]:
			temp[idx] = nums[left]
			idx += 1
			left += 1
		else:
			temp[idx] = nums[right]
			idx += 1
			right += 1
	while left <= mid:
		temp[idx] = nums[left]
		idx += 1
		left += 1
	while right <= end:
		temp[idx] = nums[right]
		idx += 1
		right += 1
	for i in range(start, end + 1):
		nums[i] = temp[i]

# print(sortIntegerMerge([1,2,4,6,4,1,2,3,45,1,1,3,44,5,76,7,3]))


class Solution3:
	def subsets(self, nums):
		if not nums:
			return [[]]
		
		results = []
		self.dfs(sorted(nums), 0, [], results)
		return results

	def dfs(self, nums, idx, candidate, results):
		results.append(candidate[:])

		for i in range(idx, len(nums)):
			if i > idx and nums[i-1] == nums[i]:
				continue
			candidate.append(nums[i])
			self.dfs(nums, i + 1, candidate, results)
			candidate.pop()

print(Solution3().subsets([1,2,2]))

class Solution4:
	def permutes(self, nums):
		if not nums:
			return [[]]
		
		results = []
		self.dfs(sorted(nums), [0]* len(nums), [], results)
		return results

	def dfs(self, nums, visited, candidate, results):
		if len(candidate) == len(nums):
			results.append(candidate[:])

		for i, num in enumerate(nums):
			if visited[i] == True:
				continue
			if i > 0 and nums[i-1] == nums[i] and visited[i-1] == False:
				continue

			visited[i] = True
			candidate.append(num)
			self.dfs(nums, visited, candidate, results)
			visited[i] = False
			candidate.pop()

print(Solution4().permutes([1,2,3,2]))


def binary_search(self, nums, target):
    if not nums:
        return -1
    
    start, end = 0, len(nums) - 1
    
    while start + 1 < end:
        mid = (start + end) // 2
        if nums[mid] < target:
            start = mid
        elif nums[mid] == target:
            return mid
        else:
            end = mid
    
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    
    return -1