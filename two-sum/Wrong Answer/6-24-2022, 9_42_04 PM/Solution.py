// https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {nums[i]:i for i in range(len(nums))}
        for i,num in enumerate(nums):
            if target-num in hashmap:
                return [i,hashmap[target-num]]