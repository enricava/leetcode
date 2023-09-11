// https://leetcode.com/problems/non-decreasing-array

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        dec = [nums[i]-nums[i+1] for i in range(len(nums)-1)]
        pos = 0
        for elem in dec:
            if elem > 0:
                pos += 1
            if pos == 2:
                return False
        return True