// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to

class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        dic = {}

        sol = []
        for i, g in enumerate(groupSizes):
            if g in dic:
                dic[g].append(i)
                if len(dic[g]) == g:
                    sol.append(dic[g])
                    dic[g] = []
            else:
                if g == 1:
                    sol.append([i])
                else:
                    dic[g] = [i]
        
        return sol
