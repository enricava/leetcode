// https://leetcode.com/problems/sign-of-the-product-of-an-array

class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg = False
        for n in nums:
            if n < 0:
                neg = not neg
            elif n == 0 :
                return 0
        
        if neg: 
            return -1
        if not neg:
            return 1