// https://leetcode.com/problems/non-decreasing-array

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        dec = [nums[i]-nums[i+1] for i in range(len(nums)-1)]
        pos = 0
        for i,elem in enumerate(dec):
            if elem > 0:
                if pos == 1:
                    return False
                pos += 1
                if i>0 and dec[i-1] + elem > 0:
                    return False
        return True