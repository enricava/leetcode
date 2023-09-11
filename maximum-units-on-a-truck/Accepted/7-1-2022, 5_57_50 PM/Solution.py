// https://leetcode.com/problems/maximum-units-on-a-truck

class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        def comp(boxType1, boxType2):
            return boxType2[1] - boxType1[1]
        
        boxTypes.sort(cmp=comp)
        
        nunits = 0
        for elem in boxTypes:
            if truckSize >= elem[0]:
                truckSize -= elem[0]
                nunits += elem[1] * elem[0]
            else:
                nunits += elem[1] * truckSize
                break
        return nunits