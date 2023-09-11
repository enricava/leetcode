// https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        useds = {}
        usedt = {}
        for c1, c2 in zip(s,t):
            if c1 not in useds and c2 not in usedt:
                useds[c1]=c2
                usedt[c2]=c1
            elif useds[c1]!=c2 or usedt[c2]!=c1:
                return False
        return True
            