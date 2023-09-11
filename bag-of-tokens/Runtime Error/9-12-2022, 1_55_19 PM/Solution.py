// https://leetcode.com/problems/bag-of-tokens

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        lo, points, ans = 0,0,0
        hi = len(tokens)-1
        while lo <= hi and (power > tokens[lo] or points > 0):
            while lo <= hi and power >= tokens[lo]:
                lo += 1
                power -= tokens[lo]
                points += 1
            ans = max(ans, points)
            
            if lo <= hi and points > 0:
                hi -= 1
                power += tokens[hi]
                points -+1
        
        return ans