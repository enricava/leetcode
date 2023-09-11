// https://leetcode.com/problems/maximize-the-confusion-of-an-exam

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        count = {'T': 0, 'F': 0}
        count[answerKey[0]] = 1
        left = 0
        right = 0
        best = 1
        n = len(answerKey)

        while right < n:
            while min(count['T'], count['F']) <= k:
                # While valid extend
                best = max(best, right-left+1)
                right += 1
                if right == n:
                    return best
                count[answerKey[right]] += 1
                
            while min(count['T'], count['F']) > k:
                # While not valid
                count[answerKey[left]] -=1
                left += 1
        
        return best
