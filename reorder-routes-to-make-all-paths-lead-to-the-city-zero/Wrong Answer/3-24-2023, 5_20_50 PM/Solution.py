// https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for con in connections:
            adj[con[0]].append(con[1])
            adj[con[1]].append(-con[0])

        vis = [0 for _ in range(n)]
        visn = [0 for _ in range(n)]
        def dfs(cur, adj, vis, visn):
            count = 0
            for a in adj[cur]:
                if a > 0:
                    if not vis[a]:
                        vis[a] = 1
                        count += 1 + dfs(a, adj, vis, visn)
                elif not visn[-a]:
                    visn[-a] =1
                    count += dfs(-a, adj, vis, visn)

            return count

        return dfs(0, adj, vis, visn)


