"""
Hi, here's your problem today. This problem was recently asked by Uber:

You have a landscape, in which puddles can form. You are given an array of non-negative integers representing the elevation at each location. Return the amount of water that would accumulate if it rains.

For example: [0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because 6 units of water can get trapped here.
       X
   X███XX█X
 X█XX█XXXXXX
# [0,1,0,2,1,0,1,3,2,1,2,1]
"""

def trap(height):
    # Fill this in.

    def trapTomax(height):
        cur_max  =0
        water = 0
        for h in height:
            if h < cur_max:
                water += cur_max - h
            else:
                cur_max = h
        return water

    if not height:
        return 0

    max_pos = height.index(max(height))

    return trapTomax(height[:max_pos]) + trapTomax(reversed(height[max_pos+1:]))




print (trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6
