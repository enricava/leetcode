// https://leetcode.com/problems/determine-if-string-halves-are-alike

class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = {'a','e','i','o','u','A','E','I','O','U'}
        ca, cb = 0,0
        n = len(s)
        for i in range(n//2):
            if s[i] in m:
                ca +=1
        for i in range(n//2, n):
            if s[i] in m:
                cb +=1
            if cb > ca:
                return False
        
        return cb == ca