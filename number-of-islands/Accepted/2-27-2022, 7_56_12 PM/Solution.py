// https://leetcode.com/problems/number-of-islands

class Solution(object):
    def dfs(self, grid, row, col, r, c):
        if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == '0':
            return 
        grid[r][c] = '0'
        self.dfs(grid, row, col, r+1, c)
        self.dfs(grid, row, col, r-1, c)
        self.dfs(grid, row, col, r, c+1)
        self.dfs(grid, row, col, r, c-1)
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        count = 0
        row = len(grid)
        col = len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    self.dfs(grid, row, col, r, c)
                    count += 1
        return count