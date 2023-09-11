// https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen = set()
        t = 0
        for c in cards:
            t+=1
            if c in seen:
                return t
            seen.add(c)
        return -1