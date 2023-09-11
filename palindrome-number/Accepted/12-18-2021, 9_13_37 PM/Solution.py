// https://leetcode.com/problems/palindrome-number

class Solution(object):
    
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        s = str(x)
        
        n = len(s)
        i = 0
        j = n-1
        while i < j:
            if s[i] != s[j]: 
                return False
            i += 1
            j -= 1
        
        return True
        