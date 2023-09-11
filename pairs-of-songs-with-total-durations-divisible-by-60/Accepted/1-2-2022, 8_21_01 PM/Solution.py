// https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        n = len(time)
        
        counted = [0 for _ in range(60)]
        count = 0
        
        for x in time:
            y = x%60
            if y == 0:
                count += counted[0]
            else :
                count += counted[60-y]
            counted[y] +=1
            
        return count