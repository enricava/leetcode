// https://leetcode.com/problems/minimum-time-to-complete-trips

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        start = 1
        end = min(time)*totalTrips

        while start < end:
            m = (start + end) //2

            if sum(m // t for t in time) >= totalTrips:
                end = m

            else:
                start = m + 1
        
        return start