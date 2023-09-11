// https://leetcode.com/problems/search-insert-position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        p = 0
        f = len(nums)
        
        while(p + 1 < f):
            m = (p+f)//2
            if nums[m] == target:
                return m
            elif nums[m]>target:
                f = m
            else :
                p = m
        return p
        