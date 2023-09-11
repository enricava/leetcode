// https://leetcode.com/problems/subarray-sum-equals-k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m = {}
        m[0] = 1
        s = 0
        r = 0
        for n in nums:
            s += n
            if s-k in m:
                r += m[s-k]
                
            if s not in m:
                m[s] = 1
            else:
                m[s] +=1
        return r