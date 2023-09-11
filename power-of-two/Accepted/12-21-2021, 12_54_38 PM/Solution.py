// https://leetcode.com/problems/power-of-two

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        v = 1
        while v < n:
            v *= 2
        
        if v == n:
            return True
        
        return False