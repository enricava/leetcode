// https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n , m = len(s), len(t)
        if n != m:
            return False
        m = [0]*26
        for i in range(n):
            m[ord(s[i])-ord('a')] += 1
            m[ord(t[i])-ord('a')] -= 1
        return True if all(v==0 for v in m) else False
            