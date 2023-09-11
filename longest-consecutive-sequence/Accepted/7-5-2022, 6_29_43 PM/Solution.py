// https://leetcode.com/problems/longest-consecutive-sequence

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        newms = set(nums)
        best = 0
        curr = 0
        streak = 0
        for num in newms:
            if num-1 not in newms:
                curr = num
                streak = 1
                
                while curr+1 in newms:
                    curr +=1
                    streak +=1
                
                best = max(best, streak)
            
        return best
        