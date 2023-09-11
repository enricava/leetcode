// https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        pos = {}
        n = len(cards)
        m = float("inf")
        for i in range(n):
            if cards[i] in pos:
                m = min(m, i - pos[cards[i]] + 1)
            pos[cards[i]] = i
        return m if m != float("inf") else -1