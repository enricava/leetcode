// https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        remaining = n - k
        total = sum(cardPoints)
        sub_sum = sum(cardPoints[:remaining])
        min_sum = sub_sum
        for i in range(remaining, n):
            sub_sum += cardPoints[i]
            sub_sum -= cardPoints[i-remaining]
            min_sum = min(min_sum, sub_sum)
        return total - min_sum
        