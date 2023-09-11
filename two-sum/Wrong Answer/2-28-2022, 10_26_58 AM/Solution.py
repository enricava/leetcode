// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums)-1
        while i < j:
            if nums[i] + nums[j] == target:
                return [i,j]
            elif nums[i] + nums[j] < target:
                i = i+1
            else :
                j = j-1