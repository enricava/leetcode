// https://leetcode.com/problems/3sum

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        
        sol = []
        n = len(nums)

        
        for i in range(0, n-1):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            k = i+1
            j = n-1
            while i < k and k < j:
                if nums[i] + nums[k] + nums[j] > 0:
                    j -= 1
                elif nums[i] + nums[k] + nums[j] < 0:
                    k += 1
                else :
                    sol.append([nums[i], nums[k], nums[j]])
                    k += 1
                    while k < j and nums[k] == nums[k-1]:
                        k += 1
        
        return sol