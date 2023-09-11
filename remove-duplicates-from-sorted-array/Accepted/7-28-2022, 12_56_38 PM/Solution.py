// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 1
        k , j = 0, 1
        while k < n:
            while j < n and nums[k] == nums[j]:
                j += 1
            if j == n:
                return k+1
            else:
                nums[k+1] = nums[j]
                k += 1
                
        return k+1
# 1 2 3 3 3 4 5
# 1 2 3 4 