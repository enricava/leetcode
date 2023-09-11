// https://leetcode.com/problems/basic-calculator-ii

class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        s = s.strip()
        l = len(s)
        curr, last, res = 0, 0, 0
        sign = '+'
        for i in range(l):
            if str.isnumeric(s[i]):
                curr = (curr*10) + ord(s[i]) - ord('0')
            if not str.isnumeric(s[i]) or i == l-1:
                if sign == '+' or sign == '-':
                    res += last
                    last = curr if sign == '+' else -curr
                elif sign == '*':
                    last = last * curr
                else:
                    last = last // curr
                sign = s[i]
                curr = 0
            
        return (res + last)