// https://leetcode.com/problems/relative-sort-array

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        m = {}
        for elem in arr1:
            if not elem in m:
                m[elem] = 1
            else:
                m[elem] += 1
        sol = []
        for elem in arr2:
            sol += [elem] * m[elem]
            del m[elem]
        
        trailing = []
        for elem in m:
            trailing += [elem] * m[elem]
            
        trailing.sort()
        
        return sol + trailing