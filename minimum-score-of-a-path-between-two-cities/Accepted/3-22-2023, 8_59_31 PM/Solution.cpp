// https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities

class Solution {
public:
    int dfs(int node,int& ans, vector<vector<pair<int, int>>>& adj, vector<int>& visited){
        visited[node] = 1;
        for(auto& [v, dis] : adj[node]){
            ans = min(ans, dis);
            if(visited[v]==0){
                visited[v] = 1;
                ans = min(ans, dfs(v, ans, adj, visited));
            }
        }
        return ans;
    }

    int minScore(int n, vector<vector<int>>& roads) {
        int ans = INT_MAX;
        vector<vector<pair<int, int>>> adj(n+1);
        for(auto edge : roads){ 
            adj[edge[0]].push_back({edge[1], edge[2]});
            adj[edge[1]].push_back({edge[0], edge[2]});
        }

        vector<int> visited(n+1, 0);
        dfs(1, ans, adj, visited);

        return ans;
    }
};