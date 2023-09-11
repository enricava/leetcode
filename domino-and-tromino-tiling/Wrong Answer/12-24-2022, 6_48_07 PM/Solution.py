// https://leetcode.com/problems/domino-and-tromino-tiling

class Solution:
    def numTilings(self, n: int) -> int:
        sol = [0,1,2,5] + [0]*(n)
        for i in range(3,n):
            sol[i+1]  = 2*sol[i] + sol[i-2]
        return sol[n]