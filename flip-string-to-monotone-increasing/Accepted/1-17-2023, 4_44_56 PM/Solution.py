// https://leetcode.com/problems/flip-string-to-monotone-increasing

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        m = 0
        for c in s:
            if c=='0':
                m += 1
                #0s on right hand side
        ans = m
        for c in s:
            if c == '0':
                m -= 1
                ans = min(m,ans)
            else:
                m += 1
        return ans