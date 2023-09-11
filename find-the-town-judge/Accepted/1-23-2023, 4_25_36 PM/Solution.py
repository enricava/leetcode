// https://leetcode.com/problems/find-the-town-judge

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        numberOfLovers = [0]*n
        lovesHowMany = [0]*n

        for pair in trust:
            numberOfLovers[pair[1]-1] +=1
            lovesHowMany[pair[0]-1] += 1

        for i in range(n):
            if numberOfLovers[i] == n-1 and lovesHowMany[i] ==0:
                return i+1
            
        return -1