// https://leetcode.com/problems/binary-search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ini = 0
        fin = len(nums)-1
        
        while ini <= fin:
            m = (ini+fin)//2
            
            if nums[m] == target:
                return m
            elif nums[m] < target:
                ini = m + 1
            else :
                fin = m - 1

        
        return -1