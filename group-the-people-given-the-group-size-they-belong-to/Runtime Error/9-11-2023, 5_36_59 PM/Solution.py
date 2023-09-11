// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to

class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        
        dic = [[] for _ in range(1, len(groupSizes)+1)]
        sol = []
        for i, g in enumerate(groupSizes):
            dic[g].append(i)
            if len(dic[g]) == g:
                sol.append(dic[g])
                dic[g] = []
        
        return sol
