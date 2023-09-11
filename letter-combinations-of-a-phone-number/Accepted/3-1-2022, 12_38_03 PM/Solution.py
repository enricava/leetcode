// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    
    m = ['','','abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        result = [c for c in self.m[int(digits[0])]]
        for i,digit in enumerate(digits):
            if i == 0:
                continue
            resultAux = []
            for code in result:
                for char in self.m[int(digit)]:
                    resultAux.append(code + char)
            result = resultAux
        return result