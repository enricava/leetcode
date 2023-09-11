// https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        used = {}
        for i, c in enumerate(s):
            if c in used and t[i] != used[c]:
                return False
            if c not in used:
                used[c] = t[i]
        return True
            