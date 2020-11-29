"""
Hi, here's your problem today. This problem was recently asked by Google:

You are given an array of tuples (start, end) representing time intervals for lectures. The intervals may be overlapping. Return the number of rooms that are required.

For example. [(30, 75), (0, 50), (60, 150)] should return 2.
"""

import heapq

def room_scheduling(lectures):
    if not lectures:
        return 0

    lectures.sort(key = lambda x: (x[0],x[1]))
    rooms_end = []
    for lecture in lectures:
        if rooms_end and rooms_end[0] <= lecture[0]:
            last_end = heapq.heappop(rooms_end)
        heapq.heappush(rooms_end,lecture[1])

    return len(rooms_end)

print(room_scheduling([(30, 75), (0, 50),(0,25), (60, 150),(25,45)]))
