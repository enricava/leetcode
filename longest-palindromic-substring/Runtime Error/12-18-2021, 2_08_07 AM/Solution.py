// https://leetcode.com/problems/longest-palindromic-substring

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        best = 1
        n = len(s)
        if n = 1:
            return s
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                best = 2
                start = i

        for k in range(3, n+1):
            for i in range(0, n-k+1):
                j = i+k-1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = 1
                    best = max(best, k)
                    start = i

        return s[start:best+1]