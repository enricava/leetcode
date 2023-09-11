// https://leetcode.com/problems/max-area-of-island

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ki = [1,-1,0,0]
        kj = [0,0,1,-1]
        m = len(grid)
        n = len(grid[0])
        
        visited = [[False for c in grid[0]] for r in grid]
        
        def ok(i,j):
            return 0<=i and i <m and 0 <=j and j < n
        
        def dfs(i,j):
            tam = 1
            visited[i][j] = True
            for k in range(4):
                if ok(i+ki[k],j+kj[k]) and not visited[i+ki[k]][j+kj[k]] and grid[i+ki[k]][j+kj[k]] == 1:
                    tam += dfs(i+ki[k],j+kj[k])
                    
            return tam
        
        best = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == 1:
                    best = max(dfs(i,j),best)
        return best