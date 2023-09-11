// https://leetcode.com/problems/minimum-absolute-difference

class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        n = len(arr)
        arr.sort()

        dif = arr[n-1] - arr[0]
        result = []

        for i in range(n-1):
            next = arr[i+1] - arr[i]
            if next > 0:
                if  next < dif:
                    result = [[arr[i], arr[i+1]]]
                    dif = next
                elif next == dif:
                    result.append([arr[i],arr[i+1]])

        return result
