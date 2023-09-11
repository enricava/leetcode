// https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for _ in range(1, numRows):
            l = map(add, [0] + res[-1], res[-1] + [0])
            res.append(list(l))
        return res if numRows else []