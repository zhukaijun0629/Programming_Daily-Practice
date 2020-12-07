"""
Hi, here's your problem today. This problem was recently asked by Google:

Given a string with a certain rule: k[string] should be expanded to string k times. So for example, 3[abc] should be expanded to abcabcabc. Nested expansions can happen, so 2[a2[b]c] should be expanded to abbcabbc.
"""

def decodeString(s):
    # Fill this in.
    stack=[]
    curnum = 0
    curstring = ''
    for c in s:
        if c.isdigit():
            curnum = curnum*10+int(c)
        elif c == '[':
            stack.append(curstring)
            stack.append(curnum)
            curstring = ''
            curnum = 0
        elif c == ']':
            num = stack.pop()
            prestring = stack.pop()
            curstring = prestring + num*curstring
        else:
            curstring += c
    return curstring



print (decodeString('2[a2[b]c]'))
# abbcabbc
