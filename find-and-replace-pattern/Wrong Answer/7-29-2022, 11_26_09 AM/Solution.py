// https://leetcode.com/problems/find-and-replace-pattern

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def mapp(w):
            m0 = {}
            v = [0] * len(w)
            k = 0
            for c in w:
                if c not in m0:
                    m0[c] = k
                    k += 1
                v[m0[c]] += 1
            return v
                
        v0 = mapp(pattern)
        sol = []
        for w in words:
            if mapp(w) == v0:
                sol.append(w)
        return sol