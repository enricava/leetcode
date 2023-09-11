// https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        i = 1
        j = x
        while i + 1 < j:
            m = (i+j)//2
            if m * m == x:
                return m
            elif m * m < x:
                i = m
            else :
                j = m
        
        return i