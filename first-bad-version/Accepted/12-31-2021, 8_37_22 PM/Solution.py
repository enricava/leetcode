// https://leetcode.com/problems/first-bad-version

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        f = n
        i = 0
        
        while True:
            m = (i+f) // 2
            if isBadVersion(m):
                if not isBadVersion(m-1):
                    return m
                f = m - 1
            else:
                if isBadVersion(m+1):
                    return m+1
                i = m + 1