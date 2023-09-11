// https://leetcode.com/problems/longest-common-prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        n = len(strs)
        
        for i in range(1,n):
            s = strs[i]
            p = len(prefix)
            q = len(s)
            m = min(p,q)
            for j in range(m):
                if prefix[j] != s[j]:
                    prefix = prefix[:j]
                    break
                if prefix == "":
                    return prefix
                           
        return prefix