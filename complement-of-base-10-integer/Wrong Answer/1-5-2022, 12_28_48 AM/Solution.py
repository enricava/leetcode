// https://leetcode.com/problems/complement-of-base-10-integer

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        i = 1
        o = 0
        while n != 0:
            if n % 2 == 0:
                o += i
            i = i * 2
            n = n // 2
        
        return o
                
                