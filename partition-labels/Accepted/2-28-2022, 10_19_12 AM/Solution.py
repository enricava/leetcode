// https://leetcode.com/problems/partition-labels

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c:i for i,c in enumerate(s)}
        start = j = 0
        res = []
        for i, c in enumerate(s):
            j = max(j, last[c])
            if i == j:
                res.append(i + 1 - start)
                start = i + 1
        return res