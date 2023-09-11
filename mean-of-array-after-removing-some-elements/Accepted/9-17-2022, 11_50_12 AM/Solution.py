// https://leetcode.com/problems/mean-of-array-after-removing-some-elements

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        l = len(arr)
        arr.sort()
        return sum(arr[l*5//100:l*95//100])/(l*0.9)