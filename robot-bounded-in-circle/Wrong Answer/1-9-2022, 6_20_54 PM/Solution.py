// https://leetcode.com/problems/robot-bounded-in-circle

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = [0,0]
        dir =[0,1]
        
        def rRight(dir):
            if dir == [0,1]:
                dir = [1,0]
            elif dir == [1,0]:
                dir = [0,-1]
            elif dir == [0,-1]:
                dir = [-1,0]
            else:
                dir = [1,0]
                
        def rLeft(dir):
            if dir == [0,1]:
                dir = [-1,0]
            elif dir == [-1,0]:
                dir = [0,-1]
            elif dir == [0,-1]:
                dir = [1,0]
            else:
                dir = [1,0]
            return dir
            
        
        for i in instructions:
            if i == 'G':
                pos[0] += dir[0]
                pos[1] += dir[1]
            elif i == 'L':
                rLeft(dir)
            else :
                rRight(dir)
        
        if pos == [0,0] or dir != [0,1]:
            return True
        
        return False