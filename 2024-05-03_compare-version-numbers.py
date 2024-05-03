'''
165. compare-version-numbers

Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.

Constraints:

1 <= version1.length, version2.length <= 500
version1 and version2 only contain digits and '.'.
version1 and version2 are valid version numbers.
All the given revisions in version1 and version2 can be stored in a 32-bit integer.
'''


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_list = version1.split(".")
        version2_list = version2.split(".")
        i = 0
        while i < max(len(version1_list) ,len(version2_list)):
            version1_num = int(version1_list[i]) if i < len(version1_list) else 0
            version2_num = int(version2_list[i]) if i < len(version2_list) else 0
            if version1_num > version2_num:
                return 1
            elif version2_num > version1_num:
                return -1
            i += 1
        return 0

# "1.0" < "1.1" ["1","0"] < ["1","1"] expects -1
print(Solution().compareVersion("1.0", "1.1"))
# 1.1.0 = 1.1 expects 0
print(Solution().compareVersion("1.1.0", "1.1"))
# 1.1.0.1 > 1.1 expects 1
print(Solution().compareVersion("1.1.0.1", "1.1"))
# 1.1 < 1.1.1 expects -1
print(Solution().compareVersion("1.1", "1.1.1"))
