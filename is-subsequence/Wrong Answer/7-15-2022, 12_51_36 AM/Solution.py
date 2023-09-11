// https://leetcode.com/problems/is-subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while j < len(t):
            while i < len(s) and s[i]==t[j]:
                i += 1
                j += 1
            if i == len(s): return True
            j += 1
        return False