// https://leetcode.com/problems/complement-of-base-10-integer

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return 2 ** (len(bin(n))-2) -1 -n
                
                