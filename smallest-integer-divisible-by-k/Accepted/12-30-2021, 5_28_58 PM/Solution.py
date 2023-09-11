// https://leetcode.com/problems/smallest-integer-divisible-by-k

class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k % 2 == 0:
            return -1
        
        n = 1
        if n % k == 0:
            return 1
        
        count = 1
        for _ in range(k):
            count += 1
            n = ((n*10) + 1) % k
            if n == 0:
                return count
        
        return -1