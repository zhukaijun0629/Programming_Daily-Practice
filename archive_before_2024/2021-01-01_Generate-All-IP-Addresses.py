"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

An IP Address is in the format of A.B.C.D, where A, B, C, D are all integers between 0 to 255.

Given a string of numbers, return the possible IP addresses you can make with that string by splitting into 4 parts of A, B, C, D.

Keep in mind that integers can't start with a 0! (Except for 0)

Example:
Input: 1592551013
Output: ['159.255.101.3', '159.255.10.13']

Leetcode #93
"""
def ip_addresses(s, ip_parts=[]):
    # Fill this in.
    def helper(s_remain,ip_parts=[]):
        if len(s_remain) > (4-len(ip_parts))*3:
            return
        if not s_remain and len(ip_parts) == 4:
            res.append(".".join(ip_parts))
        for i in range(1, min(len(s_remain),3)+1):
            if s_remain[:i]=='0' or s_remain[0] != '0' and int(s_remain[:i])<256:
                helper(s_remain[i:],ip_parts+[s_remain[:i]])

    res = []
    helper(s)
    return res

print (ip_addresses('1592551013'))
# ['159.255.101.3', '159.255.10.13']
