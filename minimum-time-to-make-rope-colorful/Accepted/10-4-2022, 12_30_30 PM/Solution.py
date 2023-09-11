// https://leetcode.com/problems/minimum-time-to-make-rope-colorful

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        m = 0
        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i-1]:
                m = 0
            time += min(m, neededTime[i])
            m = max(m, neededTime[i])
                
        return time