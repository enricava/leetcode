// https://leetcode.com/problems/summary-ranges

class Solution:
    def range(self, a,b):
        if a == b:
            return str(a)
        else :
            return str(a) + '->' + str(b)
        
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        start = 0
        ranges = []
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] > 1:
                ranges.append(self.range(nums[start],nums[i-1]))
                start = i
        ranges.append(self.range(nums[start], nums[-1]))
        return ranges