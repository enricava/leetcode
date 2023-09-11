// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique

class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        freqs = {}
        for char in s:
            if char not in freqs:
                freqs[char] = 1
            else :
                freqs[char] += 1
        
        used = {}
        deleted = 0
        for char in freqs:
            f = freqs[char]
            while f != 0 and f in used:
                f -= 1
                deleted += 1
            if f != 0:
                used[f] = True
        
        return deleted
                    