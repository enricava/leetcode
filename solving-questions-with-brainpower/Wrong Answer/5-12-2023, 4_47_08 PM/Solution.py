// https://leetcode.com/problems/solving-questions-with-brainpower

class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """

        visited = [0] * len(questions)

        def visit(i):
            best = questions[i][0]
            for k in range(i + 1 + questions[i][1], len(questions)):
                if visited[k] < questions[i][0]:
                    visited[k] = questions[i][0]
                    best = max(best, questions[i][0] + visit(k))
            return best
        
        best = 0
        for i in range(len(questions)):
            best = max(best, visit(i))

        return best