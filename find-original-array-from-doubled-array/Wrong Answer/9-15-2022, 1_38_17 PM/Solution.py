// https://leetcode.com/problems/find-original-array-from-doubled-array

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 != 0:
            return []
        m = {}
        for elem in changed:
            if elem in m:
                m[elem] +=1
            else:
                m[elem] = 1
        
        array = []
        for k in sorted(m.keys()):
            if m[k] == 0:
                continue
            if k*2 in m and m[k] == m[k*2]:
                m[k*2] = 0
                array.append(k)
            else:
                return []
        
        return array
                
        
        