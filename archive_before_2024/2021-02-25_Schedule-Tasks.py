"""
Hi, here's your problem today. This problem was recently asked by Amazon:

A task is a some work to be done which can be assumed takes 1 unit of time. Between the same type of tasks you must take at least n units of time before running the same tasks again.

Given a list of tasks (each task will be represented by a string), and a positive integer n representing the time it takes to run the same task again, find the minimum amount of time needed to run all tasks.

Leetcode #621
"""

import collections
from heapq import heappop, heappush

def schedule_tasks(tasks, n):
    # Fill this in.
    task_counts = list(collections.Counter(tasks).values())
    max_count = max(task_counts)
    num_max_count = task_counts.count(max_count)
    return max(len(tasks), (n + 1) * (max_count - 1) + num_max_count)


def schedule_tasks2(tasks, n):
    task2count = collections.Counter(tasks)
    maxHeap = []
    total_time = 0
    for task, count in task2count.items():
        heappush(maxHeap, (-count, task))
    
    while maxHeap:
        cur_time = 0
        stack = []
        while cur_time <= n:
            total_time += 1
            if maxHeap:
                count, task = heappop(maxHeap)
                if count != -1:
                    stack.append((count + 1, task))
            if not maxHeap and not stack:
                break
            cur_time += 1
             
        for item in stack:
            heappush(maxHeap, item)
    return total_time
        


print(schedule_tasks2(["A","A","A","A","A","A","B","B","B","B","B","B","C","C","C","D","E","F","G"],2))
# print 6
# one of the possible orders to run the task would be
# 'q', 'w', idle, idle, 'q', 'w'
