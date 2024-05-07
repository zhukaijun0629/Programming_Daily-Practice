"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

You are given an array of intervals - that is, an array of tuples (start, end). The array may not be sorted, and could contain overlapping intervals. Return another array where the overlapping intervals are merged.

For example:
[(1, 3), (5, 8), (4, 10), (20, 25)]

This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10) can be merged into (4, 10).
"""

def merge(intervals):
        intervals.sort()
        i=0
        j=len(intervals)
        if j<=1:
            return intervals
        while i<j-1:
            if intervals[i][1]>=intervals[i+1][0]:
                tuple1=intervals.pop(i)
                tuple2=intervals.pop(i)
                tuple3=(tuple1[0],max(tuple1[1],tuple2[1]))
                intervals.insert(i,tuple3)
                j-=1
            else:
                i+=1
        return intervals

print (merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
# [(1, 3), (4, 10), (20, 25)]
