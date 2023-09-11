// https://leetcode.com/problems/number-of-provinces

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        count = 0
        n = len(isConnected)
        visited = [0]*n
        
        def dfs(i):
            visited[i] = 1
            for j in range(n):
                if not visited[j] and isConnected[i][j]:
                    dfs(j)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
                
        
        return count