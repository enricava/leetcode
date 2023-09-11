// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        best = [0 for _ in cost] + [0]
        for i in range(2, len(cost)+1):
            best[i] = min(best[i-2]+cost[i-2], best[i-1]+cost[i-1]) 
        return best[len(cost)]