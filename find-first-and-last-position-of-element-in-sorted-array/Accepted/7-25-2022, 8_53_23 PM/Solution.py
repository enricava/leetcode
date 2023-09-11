// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
     
        if not nums:
            return [-1,-1]

        i , j = 0, len(nums)-1
        while i < j:
            m = (i+j)//2
            if nums[m] < target:
                i = m+1
            else:
                j = m
                
        if nums[i] != target:
            return [-1,-1]
        
        fi = i
        j = len(nums)-1
        while i < j:
            m = (i+j)//2 +1
            if nums[m] > target:
                j = m - 1
            else:
                i = m
        
        return [fi,j]