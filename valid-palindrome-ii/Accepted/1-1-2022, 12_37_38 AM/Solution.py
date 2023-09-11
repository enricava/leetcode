// https://leetcode.com/problems/valid-palindrome-ii

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def test(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return test(s,i+1,j) or test(s, i, j-1)
            i += 1
            j -= 1
            
        return True
        
        
                