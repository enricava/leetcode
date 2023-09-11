// https://leetcode.com/problems/valid-perfect-square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        j = num
        while i + 1 < j:
            m = (i+j)//2
            if m * m == num:
                return True
            elif m * m < num:
                i = m
            else :
                j = m
        
        return i * i == num or j * j == num