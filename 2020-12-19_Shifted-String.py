"""
Hi, here's your problem today. This problem was recently asked by Apple:

You are given two strings, A and B. Return whether A can be shifted some number of times to get B.

Eg. A = abcde, B = cdeab should return true because A can be shifted 3 times to the right to get B. A = abc and B= acb should return false.
"""
def is_shifted(A, B):
    # Fill this in.
    if sorted(A) != sorted(B): return False
    if len(A)==0: return True
    else:
        for i in range(len(A)):
            if (A[i:]+A[:i])==B:
                return True
    return False

print (is_shifted('abcde', 'cdeab'))
# True
