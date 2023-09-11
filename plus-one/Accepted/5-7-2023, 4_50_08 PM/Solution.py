// https://leetcode.com/problems/plus-one

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(digits) + 1):
            if digits[-i] != 9:
                digits[-i] += 1
                return digits
            else:
                digits[-i] = 0
        return [1] + digits
