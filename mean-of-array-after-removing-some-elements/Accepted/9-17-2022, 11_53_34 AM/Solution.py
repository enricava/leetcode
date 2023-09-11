// https://leetcode.com/problems/mean-of-array-after-removing-some-elements

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        l = len(arr)
        arr.sort()
        r = l//20
        for i in range(r):
            arr.pop(0)
            arr.pop(-1)
        return sum(arr)/(len(arr))