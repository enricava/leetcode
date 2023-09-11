// https://leetcode.com/problems/maximum-population-year

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        vals = [0]*100
        for l in logs:
            vals[l[0]-1950] += 1
            vals[l[1]-1950] -= 1
            
        res = 0
        for i in range(1,len(vals)):
            vals[i] += vals[i-1]
            res = i if vals[i] > vals[res] else res
        
        return res+1950