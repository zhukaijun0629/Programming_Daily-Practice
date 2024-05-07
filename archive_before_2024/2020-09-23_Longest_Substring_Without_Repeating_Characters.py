"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

Given a string, find the length of the longest substring without repeating characters.

Here is an example solution in Python language. (Any language is OK to use in an interview, though we'd recommend Python as a generalist language utilized by companies like Google, Facebook, Netflix, Dropbox, Pinterest, Uber, etc.,)
"""

import time
import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

class Solution1:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.
    # print(len(s))
    ans=0
    # for i in range(len(s)):
    i=0
    while i < len(s):
        # print(i)
        j=i+1
        while j < len(s):
            if s[j] in s[i:j]:
                ans=max(len(s[i:j]),ans)
                i+=s[i:j].index(s[j])
                break
            j+=1
        i+=1
    return ans

class Solution2:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.
    # print(len(s))
    ans=0
    # for i in range(len(s)):
    i=0
    for i in range(len(s)):
        # print(i)
        for j in range(i+1,len(s)):
            if s[j] in s[i:j]:
                ans=max(len(s[i:j]),ans)
                break
    return ans

a=get_random_string(1000000)
start_time1 = time.time()
print(Solution1().lengthOfLongestSubstring(a))
print("--- %s seconds ---" % (time.time() - start_time1))
start_time2 = time.time()
print(Solution2().lengthOfLongestSubstring(a))
print("--- %s seconds ---" % (time.time() - start_time2))
# 10
