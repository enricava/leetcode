// https://leetcode.com/problems/car-pooling

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        in_car, increase = 0, [0] * 1001
        for [n, fro, to] in trips: 
            increase[fro] += n
            increase[to] -= n
        for i in range(0, 1001): 
            in_car += increase[i]
            if in_car > capacity:
                return False 
        return True