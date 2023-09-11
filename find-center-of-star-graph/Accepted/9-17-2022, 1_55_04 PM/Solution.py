// https://leetcode.com/problems/find-center-of-star-graph

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        m = {}
        for edge in edges:
            if edge[0] in m:
                m[edge[0]] +=1
            else:
                m[edge[0]] =1

            if edge[1] in m:
                m[edge[1]] += 1
            else:
                m[edge[1]] = 1
                
        for i in m:
            if m[i]==len(m.keys())-1:
                return i