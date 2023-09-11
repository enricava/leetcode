// https://leetcode.com/problems/search-insert-position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        
        lo = 0
        hi = len(nums)-1
        
        while lo < hi:
            
            m = (hi+lo)//2

            if nums[m] > target:
                hi = m-1

            elif nums[m] < target:
                lo = m+1

            else:
                return m
        
        return hi