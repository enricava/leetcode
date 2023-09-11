// https://leetcode.com/problems/domino-and-tromino-tiling

class Solution:
    def numTilings(self, n: int) -> int:
        sol = [1,2,5]
        for i in range(4,n):
            if i % 3 == 1:
                sol[i] = sol[i-1]
            if i % 3 == 2:
                sol[i] = (sol[i-2] * sol[1]) % (1_000_000_007)
            else:
                sol[i] = (sol[i-3] * sol[2]) % (1_000_000_007)
        return sol[n-1]