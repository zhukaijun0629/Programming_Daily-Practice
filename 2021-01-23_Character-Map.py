"""
Hi, here's your problem today. This problem was recently asked by Google:

Given two strings, find if there is a one-to-one mapping of characters
between the two strings.

Example
Input: abc, def
Output: True # a -> d, b -> e, c -> f

Input: aab, def
Ouput: False # a can't map to d and e
"""


def has_character_map(str1, str2):
    # Method 1
    if len(str1) != len(str2):
        return False
    mp_1_to_2 = {}
    mp_2_to_1 = {}

    for i in range(len(str1)):
        if str1[i] in mp_1_to_2 and mp_1_to_2[str1[i]] != str2[i]:
            return False
        if str2[i] in mp_2_to_1 and mp_2_to_1[str2[i]] != str1[i]:
            return False
        mp_1_to_2[str1[i]] = str2[i]
        mp_2_to_1[str2[i]] = str1[i]

    return True

    # Method 2
    # return len((set(zip(str1, str2)))) == len(set(str1)) == len(set(str2))


print(has_character_map('abc', 'def'))
# True
print(has_character_map('aac', 'def'))
# False
