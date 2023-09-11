// https://leetcode.com/problems/course-schedule-ii

class Solution:
    possible = True
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []
        
        adjList = {i:[] for i in range(numCourses)}
        for pair in prerequisites:
            adjList[pair[0]].append(pair[1])

        visited = [0] * numCourses
        answer = []
        
        
        def dfs(s):
            visited[s] = 1
            for course in adjList[s]:
                if visited[course] == 0:
                    dfs(course)
                elif visited[course] == 1:
                    self.possible = False
            visited[s] = 2
            answer.append(s)

        for s in range(numCourses):
            if visited[s] == 0:
                dfs(s)

        return answer if self.possible else []