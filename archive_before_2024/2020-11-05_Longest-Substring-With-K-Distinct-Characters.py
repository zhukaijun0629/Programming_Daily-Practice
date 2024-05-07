"""
Hi, here's your problem today. This problem was recently asked by Amazon:

You are given a string s, and an integer k. Return the length of the longest substring in s that contains at most k distinct characters.

For instance, given the string:
aabcdefff and k = 3, then the longest substring with 3 distinct characters would be defff. The answer should be 5.
"""

def longest_substring_with_k_distinct_characters(s, k):
    # Fill this in.
    ans=0
    stack=[]
    s+='#'
    for i,l in enumerate(s[:-1]):
        print(l)
        if len(set(stack))<3 or l in stack:
            stack.append(l)
        if len(set(stack))==3 and s[i+1] not in stack:
            print(stack)
            ans=max(ans,len(stack))
            while len(set(stack))>=3:
                stack.pop(0)
                print(stack)
    return ans



print (longest_substring_with_k_distinct_characters('aabcdefffee', 3))
# 5 (because 'defff' has length 5 with 3 characters)
