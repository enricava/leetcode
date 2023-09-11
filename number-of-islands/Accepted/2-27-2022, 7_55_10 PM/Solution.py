// https://leetcode.com/problems/number-of-islands

class Solution(object):
    kx = [0, 0, 1, -1]
    ky = [1, -1, 0, 0]
    
    
    def ok(self, i,j, m, n):
        return 0 <= i and i < m and 0 <= j and j < n
    
    def adj(self, i,j, m, n):
        positions = []
        for k in range(4):
            if self.ok(i + self.kx[k], j + self.ky[k], m, n):
                positions.append([i + self.kx[k], j + self.ky[k]])
        return positions
    
    def bfs(self, i, j, grid, visited):
        queue = [[i,j]]
        while queue:
            top = queue.pop()
            x, y = top[0], top[1]
            if not visited[x][y]:
                visited[x][y] = 1
                if grid[x][y] == '1':
                    queue += self.adj(x,y,len(grid), len(grid[0]))
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # O(m * n)
        
        
        m = len(grid)
        n = len(grid[0])
        
        visited = [[0 for _ in range(n)] for _ in range(m)]
        
        islands = 0

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    islands += 1

                    self.bfs(i,j, grid, visited)
        return islands
                    
        # 1 1 0 0 0
        # 1 1 0 0 0 
        # 0 0 1 0 0
        # 0 0 0 1 1
                    
                    
                    
                    