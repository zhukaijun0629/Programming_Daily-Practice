'''
1404. Number of Steps to Reduce a Number in Binary Representation to One

Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

If the current number is even, you have to divide it by 2.

If the current number is odd, you have to add 1 to it.

It is guaranteed that you can always reach one for all test cases.

Constraints:

1 <= s.length <= 500
s consists of characters '0' or '1'
s[0] == '1'
'''


class Solution:
    def numSteps(self, s: str) -> int:
        value = int(s,2)
        step = 0
        while value > 1:
            if value % 2 == 0:
                value //= 2
            else:
                value += 1
            step += 1
        return step
        
'''
11
1: 11 + 1
2: 10/2 + 2/2 = 1+1
3: 10/2 = 1
'''

'''
1000
1:100
2:10
3:1
'''

'''
1001
1: 1001 + 1 = 1010
2: 1000/2 + 10/2 = 100 + 1
3: 101 + 1 = 110
4: 100/2 + 10/2 = 10 + 1
5: 11 + 1 = 100
6: 10/2 + 10/2 = 10
7: 10/2 = 1
'''