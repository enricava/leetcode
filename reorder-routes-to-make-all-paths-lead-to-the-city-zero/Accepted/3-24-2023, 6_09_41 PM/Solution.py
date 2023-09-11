// https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for con in connections:
            adj[con[0]].append(con[1])
            adj[con[1]].append(-con[0])

        vis = [0 for _ in range(n)]
        def dfs(cur, adj, vis):
            count = 0
            for a in adj[cur]:
                if not vis[abs(a)]:
                    vis[abs(a)] = 1
                    count += (1*(a>0)) + dfs(abs(a), adj, vis)

            return count

        vis[0] = 1
        return dfs(0, adj, vis)


