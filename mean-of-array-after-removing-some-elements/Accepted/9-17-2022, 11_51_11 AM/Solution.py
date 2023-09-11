// https://leetcode.com/problems/mean-of-array-after-removing-some-elements

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        l = len(arr)
        arr.sort()
        r = l*5//100
        return sum(arr[r:-r])/(l*0.9)