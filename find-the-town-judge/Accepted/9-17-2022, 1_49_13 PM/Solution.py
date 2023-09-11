// https://leetcode.com/problems/find-the-town-judge

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustedby = [0] * (n+1)
        trusts = [0] * (n+1)

        for pair in trust:
            trustedby[pair[1]] += 1
            trusts[pair[0]] += 1
        
        for i in range(1,n+1):
            if trustedby[i] == n-1 and trusts[i]==0:
                return i
        
        return -1