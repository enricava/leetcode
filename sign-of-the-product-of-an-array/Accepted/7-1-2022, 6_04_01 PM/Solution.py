// https://leetcode.com/problems/sign-of-the-product-of-an-array

class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        v = 1
        for n in nums:
            if n < 0:
                v *= -1
            if n == 0 :
                return 0
        return v