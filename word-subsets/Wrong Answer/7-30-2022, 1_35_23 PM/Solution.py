// https://leetcode.com/problems/word-subsets

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(w):
            ret = [0]*26
            for c in w:
                ret[ord(c)-ord('a')]+=1
            return ret
        
        brep = [0]*26 #minimum requirement to be universal
        for w in words2:
            for i,cc in enumerate(count(w)):
                brep[i] |= cc
        
        result = []
        for w in words1:
            if all(x >= y for x,y in zip(count(w),brep)):
                result.append(w)
        return result