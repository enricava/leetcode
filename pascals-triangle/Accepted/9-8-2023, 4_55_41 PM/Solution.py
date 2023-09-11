// https://leetcode.com/problems/pascals-triangle

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        
        prev = self.generate(numRows-1)
        cur = [1]*numRows
        for i in range(1, numRows-1):
            cur[i] = prev[-1][i-1] + prev[-1][i]
        
        return prev + [cur]