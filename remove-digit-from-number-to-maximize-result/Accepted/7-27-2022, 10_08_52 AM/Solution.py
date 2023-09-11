// https://leetcode.com/problems/remove-digit-from-number-to-maximize-result

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        m = ""
        for i in range(len(number)):
            if number[i] == digit:
                m = max(number[:i]+number[i+1:], m)
        return m