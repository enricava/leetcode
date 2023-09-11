// https://leetcode.com/problems/minimum-penalty-for-a-shop

class Solution:
    def bestClosingTime(self, customers: str) -> int:

        # initial penalty j = 0
        minP = customers.count('Y')
        curP = minP
        minH = 0

        #        N Y N Y Y Y
        # j = 0: 0 1 0 1 1 1 => minP = 4
        # j = 1: 1 1 0 1 1 1 => minP = 5
        # j = 6: 1 0 1 0 0 0 => minP = 2

        #        Y Y N Y Y Y
        # j = 0: ..          => minP = 5
        # j = 1: 0 1 0 1 1 1 => minP = 4

        for j in range(1, len(customers) + 1):
            if customers[j- 1] == 'N':
                curP += 1
            else:
                curP -= 1

            if minP > curP:
                minH = j
                minP = curP
        
        return minH

