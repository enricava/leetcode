// https://leetcode.com/problems/maximal-square

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        n = len(matrix)
        m = len(matrix[0])
        best = 0
        dp = [[0 for j in range(m+1)] for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
                    best = max(dp[i][j], best)
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

        return best
        