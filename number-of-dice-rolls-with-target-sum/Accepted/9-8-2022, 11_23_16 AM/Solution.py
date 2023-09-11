// https://leetcode.com/problems/number-of-dice-rolls-with-target-sum

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @lru_cache(None)
        def dfs(t, d):
            if t == 0 and d == 0: return 1
            if d <= 0 or t <= 0: return 0
            return sum(dfs(t-i, d-1) for i in range(1, k+1))
            
        return dfs(target, n) % int(1e9 + 7)