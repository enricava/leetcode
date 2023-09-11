// https://leetcode.com/problems/jump-game-vi

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp =[-100000000 for _ in nums]
        dp[0] = nums[0]
        for i in range(len(nums)):
            j = 1
            while j <= k and i - j >= 0:
                dp[i] = max(dp[i], dp[i-j] + nums[i])
                j+=1
        return dp[len(nums)-1]