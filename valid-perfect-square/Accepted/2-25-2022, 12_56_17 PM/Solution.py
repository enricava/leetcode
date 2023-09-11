// https://leetcode.com/problems/valid-perfect-square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i * i < num:
            i = i+1
        
        return i*i == num