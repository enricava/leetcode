// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c = Counter(s)
        m = 0
        for e in t:
            if c[e] > 0:
                c[e] -= 1
            else:
                m +=1
        return m