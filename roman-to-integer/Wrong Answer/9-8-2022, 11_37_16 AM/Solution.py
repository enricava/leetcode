// https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        
        res = 0
        more = False
        for i in range(len(s)-1):
            if m[s[i]] < m[s[i+1]]:
                res += m[s[i+1]] - m[s[i]]
                i += 1
                more = False
            else:
                res += m[s[i]]
                more = True
        if more:
            res += m[s[len(s)-1]]
                
        return res
        