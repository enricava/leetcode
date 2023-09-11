// https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = {i:[] for i in range(numCourses)}
        for pair in prerequisites:
            adjList[pair[0]].append(pair[1])

        visited = [False] * numCourses
        rec = [False] * numCourses

        def cyclic(s):
            visited[s] = True
            rec[s] = True
            print(s, visited, rec)
            for course in adjList[s]:
                if not visited[course]:
                    if cyclic(course):
                        return True
                elif rec[course]:
                    return True
            rec[s] = False
            return False



        for s in range(numCourses):
            if not visited[s]:
                if cyclic(s):
                    return False

        return True
        